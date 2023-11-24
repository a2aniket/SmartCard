# \StudentApi

All URIs are relative to *https://petstore3.swagger.io/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_student**](StudentApi.md#add_student) | **POST** /student | Add a new student
[**delete_student**](StudentApi.md#delete_student) | **DELETE** /student/{studentId} | Deletes a student
[**get_student**](StudentApi.md#get_student) | **GET** /student/{studentId} | Find student by ID
[**get_student_list**](StudentApi.md#get_student_list) | **GET** /student | Get list of all students
[**update_student**](StudentApi.md#update_student) | **PUT** /student | Update an existing student



## add_student

> crate::models::Student add_student(student)
Add a new student

Add a new student

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**student** | [**Student**](Student.md) | Create a new student | [required] |

### Return type

[**crate::models::Student**](Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
- **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_student

> crate::models::Student delete_student(student_id)
Deletes a student

delete a student

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**student_id** | **i64** | Student id to delete | [required] |

### Return type

[**crate::models::Student**](Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_student

> crate::models::Student get_student(student_id)
Find student by ID

Returns a single student

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**student_id** | **i64** | ID of student to return | [required] |

### Return type

[**crate::models::Student**](Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_student_list

> Vec<crate::models::Student> get_student_list()
Get list of all students

Returns list of students

### Parameters

This endpoint does not need any parameter.

### Return type

[**Vec<crate::models::Student>**](Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## update_student

> crate::models::Student update_student(student)
Update an existing student

Update an existing student by Id

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**student** | [**Student**](Student.md) | Update an existent student | [required] |

### Return type

[**crate::models::Student**](Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
- **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

