// Copyright 2020 The Merlin Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// +build integration integration_local

package service

import (
	"context"
	"testing"

	"github.com/google/uuid"
	"github.com/jinzhu/gorm"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/mock"

	"github.com/gojek/merlin/config"
	"github.com/gojek/merlin/it/database"
	"github.com/gojek/merlin/mlp"
	mlpMock "github.com/gojek/merlin/mlp/mocks"
	"github.com/gojek/merlin/models"
)

func TestVersionsService_FindById(t *testing.T) {
	isDefaultTrue := true
	database.WithTestDatabase(t, func(t *testing.T, db *gorm.DB) {
		env := models.Environment{
			Name:      "env1",
			Cluster:   "k8s",
			IsDefault: &isDefaultTrue,
		}
		db.Create(&env)

		p := mlp.Project{
			Id:                1,
			Name:              "project_1",
			MlflowTrackingUrl: "http://mlflow:5000",
		}

		m := models.Model{
			ProjectID:    models.ID(p.Id),
			ExperimentID: 1,
			Name:         "model_1",
			Type:         "other",
		}
		db.Create(&m)

		v := models.Version{
			ModelID:     m.ID,
			RunID:       "1",
			ArtifactURI: "gcs:/mlp/1/1",
		}
		db.Create(&v)

		endpoint1 := &models.VersionEndpoint{
			ID:              uuid.New(),
			VersionID:       v.ID,
			VersionModelID:  m.ID,
			Status:          models.EndpointTerminated,
			EnvironmentName: env.Name,
		}
		db.Create(&endpoint1)

		endpoint2 := &models.VersionEndpoint{
			ID:              uuid.New(),
			VersionID:       v.ID,
			VersionModelID:  m.ID,
			Status:          models.EndpointTerminated,
			EnvironmentName: env.Name,
		}
		db.Create(&endpoint2)

		endpoint3 := &models.VersionEndpoint{
			ID:              uuid.New(),
			VersionID:       v.ID,
			VersionModelID:  m.ID,
			Status:          models.EndpointTerminated,
			EnvironmentName: env.Name,
			Transformer: &models.Transformer{
				Enabled: true,
				Image:   "ghcr.io/gojek/merlin-transformer-test",
			},
		}
		db.Create(&endpoint3)

		mockMlpAPIClient := &mlpMock.APIClient{}
		mockMlpAPIClient.On("GetProjectByID", mock.Anything, int32(m.ProjectID)).Return(p, nil)

		versionsService := NewVersionsService(db, mockMlpAPIClient)

		found, err := versionsService.FindByID(context.Background(), m.ID, v.ID, config.MonitoringConfig{MonitoringEnabled: true})
		assert.NoError(t, err)

		assert.NotNil(t, found)
		assert.Equal(t, "http://mlflow:5000/#/experiments/1/runs/1", found.MlflowURL)
		assert.Equal(t, 3, len(found.Endpoints))

		var transformer *models.Transformer
		for _, endpoint := range found.Endpoints {
			if endpoint.Transformer != nil {
				transformer = endpoint.Transformer
			}
		}
		assert.Equal(t, endpoint3.Transformer.Image, transformer.Image)
	})
}

func TestVersionsService_ListVersions(t *testing.T) {
	isDefaultTrue := true
	database.WithTestDatabase(t, func(t *testing.T, db *gorm.DB) {
		env := models.Environment{
			Name:      "env1",
			Cluster:   "k8s",
			IsDefault: &isDefaultTrue,
		}
		db.Create(&env)

		p := mlp.Project{
			Id:                1,
			Name:              "project_1",
			MlflowTrackingUrl: "http://mlflow:5000",
		}

		m := models.Model{
			ProjectID:    models.ID(p.Id),
			ExperimentID: 1,
			Name:         "model_1",
			Type:         "other",
		}
		db.Create(&m)

		numOfVersions := 10
		for i := 0; i < numOfVersions; i++ {
			v := models.Version{
				ModelID:     m.ID,
				RunID:       "1",
				ArtifactURI: "gcs:/mlp/1/1",
			}
			db.Create(&v)
			endpoint1 := &models.VersionEndpoint{
				ID:              uuid.New(),
				VersionID:       v.ID,
				VersionModelID:  m.ID,
				Status:          models.EndpointTerminated,
				EnvironmentName: env.Name,
			}
			db.Create(&endpoint1)

			endpoint2 := &models.VersionEndpoint{
				ID:              uuid.New(),
				VersionID:       v.ID,
				VersionModelID:  m.ID,
				Status:          models.EndpointTerminated,
				EnvironmentName: env.Name,
			}
			db.Create(&endpoint2)

			endpoint3 := &models.VersionEndpoint{
				ID:              uuid.New(),
				VersionID:       v.ID,
				VersionModelID:  m.ID,
				Status:          models.EndpointTerminated,
				EnvironmentName: env.Name,
				Transformer: &models.Transformer{
					Enabled: true,
					Image:   "ghcr.io/gojek/merlin-transformer-test",
				},
			}
			db.Create(&endpoint3)
		}

		mockMlpAPIClient := &mlpMock.APIClient{}
		mockMlpAPIClient.On("GetProjectByID", mock.Anything, int32(m.ProjectID)).Return(p, nil)

		versionsService := NewVersionsService(db, mockMlpAPIClient)

		numOfFetchedVersions := 0
		cursor := ""
		limit := 3
		for numOfFetchedVersions < numOfVersions {
			versions, nextCursor, err := versionsService.ListVersions(context.Background(), m.ID, config.MonitoringConfig{MonitoringEnabled: true}, VersionQuery{
				Limit:  limit,
				Cursor: cursor,
			})
			assert.NoError(t, err)

			expectedNumOfReturns := limit
			if numOfFetchedVersions+limit > numOfVersions {
				expectedNumOfReturns = numOfVersions - numOfFetchedVersions
			}
			assert.Equal(t, expectedNumOfReturns, len(versions))
			cursor = nextCursor
			numOfFetchedVersions = numOfFetchedVersions + len(versions)
		}
	})
}
