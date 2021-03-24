// Code generated by mockery v2.6.0. DO NOT EDIT.

package mocks

import (
	mlp "github.com/gojek/merlin/mlp"
	mock "github.com/stretchr/testify/mock"

	models "github.com/gojek/merlin/models"

	queue "github.com/gojek/merlin/queue"

	service "github.com/gojek/merlin/service"
)

// PredictionJobService is an autogenerated mock type for the PredictionJobService type
type PredictionJobService struct {
	mock.Mock
}

// CreatePredictionJob provides a mock function with given fields: env, model, version, predictionJob
func (_m *PredictionJobService) CreatePredictionJob(env *models.Environment, model *models.Model, version *models.Version, predictionJob *models.PredictionJob) (*models.PredictionJob, error) {
	ret := _m.Called(env, model, version, predictionJob)

	var r0 *models.PredictionJob
	if rf, ok := ret.Get(0).(func(*models.Environment, *models.Model, *models.Version, *models.PredictionJob) *models.PredictionJob); ok {
		r0 = rf(env, model, version, predictionJob)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(*models.PredictionJob)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(*models.Environment, *models.Model, *models.Version, *models.PredictionJob) error); ok {
		r1 = rf(env, model, version, predictionJob)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// ExecuteDeployment provides a mock function with given fields: job
func (_m *PredictionJobService) ExecuteDeployment(job *queue.Job) error {
	ret := _m.Called(job)

	var r0 error
	if rf, ok := ret.Get(0).(func(*queue.Job) error); ok {
		r0 = rf(job)
	} else {
		r0 = ret.Error(0)
	}

	return r0
}

// GetPredictionJob provides a mock function with given fields: env, model, version, id
func (_m *PredictionJobService) GetPredictionJob(env *models.Environment, model *models.Model, version *models.Version, id models.ID) (*models.PredictionJob, error) {
	ret := _m.Called(env, model, version, id)

	var r0 *models.PredictionJob
	if rf, ok := ret.Get(0).(func(*models.Environment, *models.Model, *models.Version, models.ID) *models.PredictionJob); ok {
		r0 = rf(env, model, version, id)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(*models.PredictionJob)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(*models.Environment, *models.Model, *models.Version, models.ID) error); ok {
		r1 = rf(env, model, version, id)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// ListContainers provides a mock function with given fields: env, model, version, predictionJob
func (_m *PredictionJobService) ListContainers(env *models.Environment, model *models.Model, version *models.Version, predictionJob *models.PredictionJob) ([]*models.Container, error) {
	ret := _m.Called(env, model, version, predictionJob)

	var r0 []*models.Container
	if rf, ok := ret.Get(0).(func(*models.Environment, *models.Model, *models.Version, *models.PredictionJob) []*models.Container); ok {
		r0 = rf(env, model, version, predictionJob)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).([]*models.Container)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(*models.Environment, *models.Model, *models.Version, *models.PredictionJob) error); ok {
		r1 = rf(env, model, version, predictionJob)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// ListPredictionJobs provides a mock function with given fields: project, query
func (_m *PredictionJobService) ListPredictionJobs(project mlp.Project, query *service.ListPredictionJobQuery) ([]*models.PredictionJob, error) {
	ret := _m.Called(project, query)

	var r0 []*models.PredictionJob
	if rf, ok := ret.Get(0).(func(mlp.Project, *service.ListPredictionJobQuery) []*models.PredictionJob); ok {
		r0 = rf(project, query)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).([]*models.PredictionJob)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(mlp.Project, *service.ListPredictionJobQuery) error); ok {
		r1 = rf(project, query)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// StopPredictionJob provides a mock function with given fields: env, model, version, id
func (_m *PredictionJobService) StopPredictionJob(env *models.Environment, model *models.Model, version *models.Version, id models.ID) (*models.PredictionJob, error) {
	ret := _m.Called(env, model, version, id)

	var r0 *models.PredictionJob
	if rf, ok := ret.Get(0).(func(*models.Environment, *models.Model, *models.Version, models.ID) *models.PredictionJob); ok {
		r0 = rf(env, model, version, id)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(*models.PredictionJob)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(*models.Environment, *models.Model, *models.Version, models.ID) error); ok {
		r1 = rf(env, model, version, id)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}
