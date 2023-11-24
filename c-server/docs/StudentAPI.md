# StudentAPI

All URIs are relative to *https://petstore3.swagger.io/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**StudentAPI_addStudent**](StudentAPI.md#StudentAPI_addStudent) | **POST** /student | Add a new student
[**StudentAPI_deleteStudent**](StudentAPI.md#StudentAPI_deleteStudent) | **DELETE** /student/{studentId} | Deletes a student
[**StudentAPI_getStudent**](StudentAPI.md#StudentAPI_getStudent) | **GET** /student/{studentId} | Find student by ID
[**StudentAPI_getStudentList**](StudentAPI.md#StudentAPI_getStudentList) | **GET** /student | Get list of all students
[**StudentAPI_updateStudent**](StudentAPI.md#StudentAPI_updateStudent) | **PUT** /student | Update an existing student


# **StudentAPI_addStudent**
```c
// Add a new student
//
// Add a new student
//
student_t* StudentAPI_addStudent(apiClient_t *apiClient, student_t * student);
```

### Parameters
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**apiClient** | **apiClient_t \*** | context containing the client configuration |
**student** | **[student_t](student.md) \*** | Create a new student | 

### Return type

[student_t](student.md) *


### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **StudentAPI_deleteStudent**
```c
// Deletes a student
//
// delete a student
//
student_t* StudentAPI_deleteStudent(apiClient_t *apiClient, long studentId);
```

### Parameters
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**apiClient** | **apiClient_t \*** | context containing the client configuration |
**studentId** | **long** | Student id to delete | 

### Return type

[student_t](student.md) *


### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **StudentAPI_getStudent**
```c
// Find student by ID
//
// Returns a single student
//
student_t* StudentAPI_getStudent(apiClient_t *apiClient, long studentId);
```

### Parameters
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**apiClient** | **apiClient_t \*** | context containing the client configuration |
**studentId** | **long** | ID of student to return | 

### Return type

[student_t](student.md) *


### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **StudentAPI_getStudentList**
```c
// Get list of all students
//
// Returns list of students
//
list_t* StudentAPI_getStudentList(apiClient_t *apiClient);
```

### Parameters
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**apiClient** | **apiClient_t \*** | context containing the client configuration |

### Return type

[list_t](student.md) *


### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **StudentAPI_updateStudent**
```c
// Update an existing student
//
// Update an existing student by Id
//
student_t* StudentAPI_updateStudent(apiClient_t *apiClient, student_t * student);
```

### Parameters
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**apiClient** | **apiClient_t \*** | context containing the client configuration |
**student** | **[student_t](student.md) \*** | Update an existent student | 

### Return type

[student_t](student.md) *


### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

