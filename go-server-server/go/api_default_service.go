/*
 * Code Generation API
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * API version: 1.0.0
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi

import (
	"context"
	"net/http"
	"errors"
)

// DefaultApiService is a service that implements the logic for the DefaultApiServicer
// This service should implement the business logic for every endpoint for the DefaultApi API.
// Include any external packages or services that will be required by this service.
type DefaultApiService struct {
}

// NewDefaultApiService creates a default api service
func NewDefaultApiService() DefaultApiServicer {
	return &DefaultApiService{}
}

// GenerateCodePost - Generate code from OpenAPI specification
func (s *DefaultApiService) GenerateCodePost(ctx context.Context, generateCodePostRequest GenerateCodePostRequest) (ImplResponse, error) {
	// TODO - update GenerateCodePost with the required logic for this service method.
	// Add api_default_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	//TODO: Uncomment the next line to return response Response(200, GenerateCodePost200Response{}) or use other options such as http.Ok ...
	//return Response(200, GenerateCodePost200Response{}), nil

	//TODO: Uncomment the next line to return response Response(400, GenerateCodePost400Response{}) or use other options such as http.Ok ...
	//return Response(400, GenerateCodePost400Response{}), nil

	return Response(http.StatusNotImplemented, nil), errors.New("GenerateCodePost method not implemented")
}
