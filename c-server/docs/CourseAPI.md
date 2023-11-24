# CourseAPI

All URIs are relative to *https://petstore3.swagger.io/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CourseAPI_addCourse**](CourseAPI.md#CourseAPI_addCourse) | **POST** /course | Add a new course
[**CourseAPI_deleteCourse**](CourseAPI.md#CourseAPI_deleteCourse) | **DELETE** /course/{courseId} | Deletes a course
[**CourseAPI_getCourse**](CourseAPI.md#CourseAPI_getCourse) | **GET** /course/{courseId} | Find course by ID
[**CourseAPI_getCourseList**](CourseAPI.md#CourseAPI_getCourseList) | **GET** /course | Get list of all courses
[**CourseAPI_updateCourse**](CourseAPI.md#CourseAPI_updateCourse) | **PUT** /course | Update an existing course


# **CourseAPI_addCourse**
```c
// Add a new course
//
// Add a new course
//
course_t* CourseAPI_addCourse(apiClient_t *apiClient, course_t * course);
```

### Parameters
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**apiClient** | **apiClient_t \*** | context containing the client configuration |
**course** | **[course_t](course.md) \*** | Create a new course | 

### Return type

[course_t](course.md) *


### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CourseAPI_deleteCourse**
```c
// Deletes a course
//
// delete a course
//
course_t* CourseAPI_deleteCourse(apiClient_t *apiClient, long courseId);
```

### Parameters
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**apiClient** | **apiClient_t \*** | context containing the client configuration |
**courseId** | **long** | Course id to delete | 

### Return type

[course_t](course.md) *


### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CourseAPI_getCourse**
```c
// Find course by ID
//
// Returns a single course
//
course_t* CourseAPI_getCourse(apiClient_t *apiClient, long courseId);
```

### Parameters
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**apiClient** | **apiClient_t \*** | context containing the client configuration |
**courseId** | **long** | ID of course to return | 

### Return type

[course_t](course.md) *


### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CourseAPI_getCourseList**
```c
// Get list of all courses
//
// Returns list of courses
//
list_t* CourseAPI_getCourseList(apiClient_t *apiClient);
```

### Parameters
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**apiClient** | **apiClient_t \*** | context containing the client configuration |

### Return type

[list_t](course.md) *


### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CourseAPI_updateCourse**
```c
// Update an existing course
//
// Update an existing course by Id
//
course_t* CourseAPI_updateCourse(apiClient_t *apiClient, course_t * course);
```

### Parameters
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**apiClient** | **apiClient_t \*** | context containing the client configuration |
**course** | **[course_t](course.md) \*** | Update an existent course | 

### Return type

[course_t](course.md) *


### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

