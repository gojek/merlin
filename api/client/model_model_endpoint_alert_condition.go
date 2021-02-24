/*
 * Merlin
 *
 * API Guide for accessing Merlin's model management, deployment, and serving functionalities
 *
 * API version: 0.7.0
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package client

type ModelEndpointAlertCondition struct {
	Enabled    bool                      `json:"enabled,omitempty"`
	MetricType *AlertConditionMetricType `json:"metric_type,omitempty"`
	Severity   *AlertConditionSeverity   `json:"severity,omitempty"`
	Target     float64                   `json:"target,omitempty"`
	Percentile float64                   `json:"percentile,omitempty"`
	Unit       string                    `json:"unit,omitempty"`
}
