# GenerateCodePostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Language** | **string** | The programming language to generate code for | 
**OpenAPIUrl** | **string** | The URL of the OpenAPI specification to generate code from | 

## Methods

### NewGenerateCodePostRequest

`func NewGenerateCodePostRequest(language string, openAPIUrl string, ) *GenerateCodePostRequest`

NewGenerateCodePostRequest instantiates a new GenerateCodePostRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGenerateCodePostRequestWithDefaults

`func NewGenerateCodePostRequestWithDefaults() *GenerateCodePostRequest`

NewGenerateCodePostRequestWithDefaults instantiates a new GenerateCodePostRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLanguage

`func (o *GenerateCodePostRequest) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *GenerateCodePostRequest) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *GenerateCodePostRequest) SetLanguage(v string)`

SetLanguage sets Language field to given value.


### GetOpenAPIUrl

`func (o *GenerateCodePostRequest) GetOpenAPIUrl() string`

GetOpenAPIUrl returns the OpenAPIUrl field if non-nil, zero value otherwise.

### GetOpenAPIUrlOk

`func (o *GenerateCodePostRequest) GetOpenAPIUrlOk() (*string, bool)`

GetOpenAPIUrlOk returns a tuple with the OpenAPIUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpenAPIUrl

`func (o *GenerateCodePostRequest) SetOpenAPIUrl(v string)`

SetOpenAPIUrl sets OpenAPIUrl field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


