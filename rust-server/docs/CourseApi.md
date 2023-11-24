# \CourseApi

All URIs are relative to *https://petstore3.swagger.io/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_course**](CourseApi.md#add_course) | **POST** /course | Add a new course
[**delete_course**](CourseApi.md#delete_course) | **DELETE** /course/{courseId} | Deletes a course
[**get_course**](CourseApi.md#get_course) | **GET** /course/{courseId} | Find course by ID
[**get_course_list**](CourseApi.md#get_course_list) | **GET** /course | Get list of all courses
[**update_course**](CourseApi.md#update_course) | **PUT** /course | Update an existing course



## add_course

> crate::models::Course add_course(course)
Add a new course

Add a new course

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**course** | [**Course**](Course.md) | Create a new course | [required] |

### Return type

[**crate::models::Course**](Course.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
- **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_course

> crate::models::Course delete_course(course_id)
Deletes a course

delete a course

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**course_id** | **i64** | Course id to delete | [required] |

### Return type

[**crate::models::Course**](Course.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_course

> crate::models::Course get_course(course_id)
Find course by ID

Returns a single course

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**course_id** | **i64** | ID of course to return | [required] |

### Return type

[**crate::models::Course**](Course.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_course_list

> Vec<crate::models::Course> get_course_list()
Get list of all courses

Returns list of courses

### Parameters

This endpoint does not need any parameter.

### Return type

[**Vec<crate::models::Course>**](Course.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## update_course

> crate::models::Course update_course(course)
Update an existing course

Update an existing course by Id

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**course** | [**Course**](Course.md) | Update an existent course | [required] |

### Return type

[**crate::models::Course**](Course.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
- **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

