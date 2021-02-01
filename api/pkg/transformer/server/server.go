package server

import (
	"bytes"
	"context"
	"fmt"
	"io/ioutil"
	"net/http"
	_ "net/http/pprof"
	"os"
	"os/signal"
	"syscall"
	"time"

	"github.com/heptiolabs/healthcheck"
	"github.com/pkg/errors"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	"go.uber.org/zap"
)

const MerlinLogIdHeader = "X-Merlin-Log-Id"

var shutdownSignals = []os.Signal{os.Interrupt, syscall.SIGTERM}
var onlyOneSignalHandler = make(chan struct{})

// Options for the server.
type Options struct {
	Port            string `envconfig:"MERLIN_TRANSFORMER_PORT" default:"8080"`
	ModelName       string `envconfig:"MERLIN_TRANSFORMER_MODEL_NAME" default:"my-model"`
	ModelPredictURL string `envconfig:"MERLIN_TRANSFORMER_MODEL_PREDICT_URL" default:"http://localhost:8081/v1/models/model:predict"`
}

// Server serves various HTTP endpoints of Feast transformer.
type Server struct {
	options    *Options
	httpClient *http.Client
	logger     *zap.Logger

	PreprocessHandler  func(ctx context.Context, request []byte) ([]byte, error)
	PostprocessHandler func(ctx context.Context, request []byte) ([]byte, error)
	LivenessHandler    func(w http.ResponseWriter, r *http.Request)
}

// New initializes a new Server.
func New(o *Options, logger *zap.Logger) *Server {
	return &Server{
		options:    o,
		httpClient: &http.Client{},
		logger:     logger,
	}
}

// PredictHandler handles prediction request to the transformer and model.
func (s *Server) PredictHandler(w http.ResponseWriter, r *http.Request) {
	ctx := r.Context()

	requestBody, err := ioutil.ReadAll(r.Body)
	if err != nil {
		s.logger.Error("read requestBody body", zap.Error(err))
		fmt.Fprintf(w, err.Error())
		return
	}
	defer r.Body.Close()
	s.logger.Debug("requestBody", zap.ByteString("requestBody", requestBody))

	preprocessedRequestBody := requestBody
	if s.PreprocessHandler != nil {
		preprocessedRequestBody, err = s.PreprocessHandler(ctx, requestBody)
		if err != nil {
			s.logger.Error("preprocess error", zap.Error(err))
			fmt.Fprintf(w, err.Error())
			return
		}
		s.logger.Debug("preprocess requestBody", zap.ByteString("preprocess_response", preprocessedRequestBody))
	}

	preprocessedRequestBody, err = s.predict(r, preprocessedRequestBody)
	if err != nil {
		s.logger.Error("predict error", zap.Error(err))
		fmt.Fprintf(w, err.Error())
		return
	}
	s.logger.Debug("predict requestBody", zap.ByteString("predict_response", preprocessedRequestBody))
	fmt.Fprintf(w, string(preprocessedRequestBody))
}

func (s *Server) predict(r *http.Request, request []byte) ([]byte, error) {

	req, err := http.NewRequest("POST", s.options.ModelPredictURL, bytes.NewBuffer(request))
	if err != nil {
		return nil, err
	}

	// propagate merlin request id header to model
	if len(r.Header.Get(MerlinLogIdHeader)) != 0 {
		req.Header.Set(MerlinLogIdHeader, r.Header.Get(MerlinLogIdHeader))
	}

	req.Header.Set("Content-Type", "application/json")

	resp, err := s.httpClient.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}

	return body, nil
}

// Run serves the HTTP endpoints.
func (s *Server) Run() {
	// use default mux
	health := healthcheck.NewHandler()
	http.Handle("/", health)
	http.HandleFunc(fmt.Sprintf("/v1/models/%s:predict", s.options.ModelName), s.PredictHandler)
	http.Handle("/metrics", promhttp.Handler())

	addr := fmt.Sprintf(":%s", s.options.Port)
	srv := &http.Server{Addr: addr, Handler: http.DefaultServeMux}

	stopCh := setupSignalHandler()
	errCh := make(chan error, 1)
	go func() {
		s.logger.Info("starting standard transformer at : " + addr)
		// Don't forward ErrServerClosed as that indicates we're already shutting down.
		if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
			errCh <- errors.Wrapf(err, "%s server failed")
		}
		s.logger.Info("server shut down successfully")
	}()

	// Exit as soon as we see a shutdown signal or the server failed.
	select {
	case <-stopCh:
	case err := <-errCh:
		s.logger.Error(fmt.Sprintf("failed to run HTTP server: %v", err))
	}

	s.logger.Info("server shutting down...")
	time.Sleep(5 * time.Second)

	if err := srv.Shutdown(context.Background()); err != nil {
		s.logger.Error(fmt.Sprintf("failed to shutdown HTTP server: %v", err))
	}
}

// setupSignalHandler registered for SIGTERM and SIGINT. A stop channel is returned
// which is closed on one of these signals. If a second signal is caught, the program
// is terminated with exit code 1.
func setupSignalHandler() (stopCh <-chan struct{}) {
	close(onlyOneSignalHandler) // panics when called twice

	stop := make(chan struct{})
	c := make(chan os.Signal, 2)
	signal.Notify(c, shutdownSignals...)
	go func() {
		<-c
		close(stop)
		<-c
		os.Exit(1) // second signal. Exit directly.
	}()

	return stop
}
