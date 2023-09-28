# \DefaultApi

All URIs are relative to *http://33.227.17.219/v1/apigen*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GenerateCodePost**](DefaultApi.md#GenerateCodePost) | **Post** /generate/code | Generate code from OpenAPI specification



## GenerateCodePost

> GenerateCodePost200Response GenerateCodePost(ctx).GenerateCodePostRequest(generateCodePostRequest).Execute()

Generate code from OpenAPI specification

### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    generateCodePostRequest := *openapiclient.NewGenerateCodePostRequest("Language_example", "OpenAPIUrl_example") // GenerateCodePostRequest | 

    configuration := openapiclient.NewConfiguration()
    apiClient := openapiclient.NewAPIClient(configuration)
    resp, r, err := apiClient.DefaultApi.GenerateCodePost(context.Background()).GenerateCodePostRequest(generateCodePostRequest).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `DefaultApi.GenerateCodePost``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `GenerateCodePost`: GenerateCodePost200Response
    fmt.Fprintf(os.Stdout, "Response from `DefaultApi.GenerateCodePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGenerateCodePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generateCodePostRequest** | [**GenerateCodePostRequest**](GenerateCodePostRequest.md) |  | 

### Return type

[**GenerateCodePost200Response**](GenerateCodePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

