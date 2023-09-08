/*
 * Swagger Petstore - OpenAPI 3.0
 *
 * This is a sample Pet Store Server based on the OpenAPI 3.0 specification.  You can find out more about Swagger at [https://swagger.io](https://swagger.io). In the third iteration of the pet store, we've switched to the design first approach! You can now help us improve the API whether it's by making changes to the definition itself or to the code. That way, with time, we can improve the API in general, and expose some of the new features in OAS3.
 *
 * API version: 1.0.11
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi

import (
	"context"
	"net/http"
	"errors"
)

// ProductApiService is a service that implements the logic for the ProductApiServicer
// This service should implement the business logic for every endpoint for the ProductApi API.
// Include any external packages or services that will be required by this service.
type ProductApiService struct {
}

// NewProductApiService creates a default api service
func NewProductApiService() ProductApiServicer {
	return &ProductApiService{}
}

// AddProduct - Add a new Product to the store
func (s *ProductApiService) AddProduct(ctx context.Context, product Product) (ImplResponse, error) {
	// TODO - update AddProduct with the required logic for this service method.
	// Add api_product_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	//TODO: Uncomment the next line to return response Response(200, Product{}) or use other options such as http.Ok ...
	//return Response(200, Product{}), nil

	//TODO: Uncomment the next line to return response Response(405, {}) or use other options such as http.Ok ...
	//return Response(405, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("AddProduct method not implemented")
}

// DeleteProduct - Deletes a Product
func (s *ProductApiService) DeleteProduct(ctx context.Context, productId int64) (ImplResponse, error) {
	// TODO - update DeleteProduct with the required logic for this service method.
	// Add api_product_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	//TODO: Uncomment the next line to return response Response(200, Product{}) or use other options such as http.Ok ...
	//return Response(200, Product{}), nil

	//TODO: Uncomment the next line to return response Response(400, {}) or use other options such as http.Ok ...
	//return Response(400, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("DeleteProduct method not implemented")
}

// GetProduct - Find Product by ID
func (s *ProductApiService) GetProduct(ctx context.Context, productId int64) (ImplResponse, error) {
	// TODO - update GetProduct with the required logic for this service method.
	// Add api_product_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	//TODO: Uncomment the next line to return response Response(200, Product{}) or use other options such as http.Ok ...
	//return Response(200, Product{}), nil

	//TODO: Uncomment the next line to return response Response(400, {}) or use other options such as http.Ok ...
	//return Response(400, nil),nil

	//TODO: Uncomment the next line to return response Response(404, {}) or use other options such as http.Ok ...
	//return Response(404, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("GetProduct method not implemented")
}

// GetProductList - Get list of all products
func (s *ProductApiService) GetProductList(ctx context.Context) (ImplResponse, error) {
	// TODO - update GetProductList with the required logic for this service method.
	// Add api_product_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	//TODO: Uncomment the next line to return response Response(200, []Product{}) or use other options such as http.Ok ...
	//return Response(200, []Product{}), nil

	//TODO: Uncomment the next line to return response Response(400, {}) or use other options such as http.Ok ...
	//return Response(400, nil),nil

	//TODO: Uncomment the next line to return response Response(404, {}) or use other options such as http.Ok ...
	//return Response(404, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("GetProductList method not implemented")
}

// UpdateProduct - Update an existing Product
func (s *ProductApiService) UpdateProduct(ctx context.Context, product Product) (ImplResponse, error) {
	// TODO - update UpdateProduct with the required logic for this service method.
	// Add api_product_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	//TODO: Uncomment the next line to return response Response(200, Product{}) or use other options such as http.Ok ...
	//return Response(200, Product{}), nil

	//TODO: Uncomment the next line to return response Response(400, {}) or use other options such as http.Ok ...
	//return Response(400, nil),nil

	//TODO: Uncomment the next line to return response Response(404, {}) or use other options such as http.Ok ...
	//return Response(404, nil),nil

	//TODO: Uncomment the next line to return response Response(405, {}) or use other options such as http.Ok ...
	//return Response(405, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("UpdateProduct method not implemented")
}
