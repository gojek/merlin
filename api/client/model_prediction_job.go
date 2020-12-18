/*
 * Merlin
 *
 * API Guide for accessing Merlin's model management, deployment, and serving functionalities
 *
 * API version: 0.7.0
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package client

import (
	"time"
)

type PredictionJob struct {
	ID              int32        `json:"id,omitempty"`
	Name            string       `json:"name,omitempty"`
	VersionID       int32        `json:"version_id,omitempty"`
	ModelID         int32        `json:"model_id,omitempty"`
	ProjectID       int32        `json:"project_id,omitempty"`
	EnvironmentName string       `json:"environment_name,omitempty"`
	Environment     *Environment `json:"environment,omitempty"`
	Config          *Config      `json:"config,omitempty"`
	Status          string       `json:"status,omitempty"`
	Error          string       `json:"error,omitempty"`
	CreatedAt       time.Time    `json:"created_at,omitempty"`
	UpdatedAt       time.Time    `json:"updated_at,omitempty"`
}
