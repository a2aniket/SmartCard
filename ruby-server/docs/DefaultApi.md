# OpenapiClient::DefaultApi

All URIs are relative to *http://34.227.17.219/v1/apigen*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**generate_code_post**](DefaultApi.md#generate_code_post) | **POST** /generate/code | Generate code from OpenAPI specification |


## generate_code_post

> <GenerateCodePost200Response> generate_code_post(generate_code_post_request)

Generate code from OpenAPI specification

### Examples

```ruby
require 'time'
require 'openapi_client'

api_instance = OpenapiClient::DefaultApi.new
generate_code_post_request = OpenapiClient::GenerateCodePostRequest.new({language: 'language_example', open_api_url: 'open_api_url_example'}) # GenerateCodePostRequest | 

begin
  # Generate code from OpenAPI specification
  result = api_instance.generate_code_post(generate_code_post_request)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling DefaultApi->generate_code_post: #{e}"
end
```

#### Using the generate_code_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GenerateCodePost200Response>, Integer, Hash)> generate_code_post_with_http_info(generate_code_post_request)

```ruby
begin
  # Generate code from OpenAPI specification
  data, status_code, headers = api_instance.generate_code_post_with_http_info(generate_code_post_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GenerateCodePost200Response>
rescue OpenapiClient::ApiError => e
  puts "Error when calling DefaultApi->generate_code_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **generate_code_post_request** | [**GenerateCodePostRequest**](GenerateCodePostRequest.md) |  |  |

### Return type

[**GenerateCodePost200Response**](GenerateCodePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

