# Org.OpenAPITools.Api.StudentApi

All URIs are relative to *https://petstore3.swagger.io/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddStudent**](StudentApi.md#addstudent) | **POST** /student | Add a new student
[**DeleteStudent**](StudentApi.md#deletestudent) | **DELETE** /student/{studentId} | Deletes a student
[**GetStudent**](StudentApi.md#getstudent) | **GET** /student/{studentId} | Find student by ID
[**GetStudentList**](StudentApi.md#getstudentlist) | **GET** /student | Get list of all students
[**UpdateStudent**](StudentApi.md#updatestudent) | **PUT** /student | Update an existing student



## AddStudent

> Student AddStudent (Student student)

Add a new student

Add a new student

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class AddStudentExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "https://petstore3.swagger.io/api/v3";
            var apiInstance = new StudentApi(Configuration.Default);
            var student = new Student(); // Student | Create a new student

            try
            {
                // Add a new student
                Student result = apiInstance.AddStudent(student);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling StudentApi.AddStudent: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **student** | [**Student**](Student.md)| Create a new student | 

### Return type

[**Student**](Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **405** | Invalid input |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteStudent

> Student DeleteStudent (long studentId)

Deletes a student

delete a student

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class DeleteStudentExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "https://petstore3.swagger.io/api/v3";
            var apiInstance = new StudentApi(Configuration.Default);
            var studentId = 789L;  // long | Student id to delete

            try
            {
                // Deletes a student
                Student result = apiInstance.DeleteStudent(studentId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling StudentApi.DeleteStudent: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studentId** | **long**| Student id to delete | 

### Return type

[**Student**](Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid student value |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetStudent

> Student GetStudent (long studentId)

Find student by ID

Returns a single student

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class GetStudentExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "https://petstore3.swagger.io/api/v3";
            var apiInstance = new StudentApi(Configuration.Default);
            var studentId = 789L;  // long | ID of student to return

            try
            {
                // Find student by ID
                Student result = apiInstance.GetStudent(studentId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling StudentApi.GetStudent: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studentId** | **long**| ID of student to return | 

### Return type

[**Student**](Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid ID supplied |  -  |
| **404** | Student not found |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetStudentList

> List&lt;Student&gt; GetStudentList ()

Get list of all students

Returns list of students

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class GetStudentListExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "https://petstore3.swagger.io/api/v3";
            var apiInstance = new StudentApi(Configuration.Default);

            try
            {
                // Get list of all students
                List<Student> result = apiInstance.GetStudentList();
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling StudentApi.GetStudentList: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**List&lt;Student&gt;**](Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid ID supplied |  -  |
| **404** | Student not found |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateStudent

> Student UpdateStudent (Student student)

Update an existing student

Update an existing student by Id

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class UpdateStudentExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "https://petstore3.swagger.io/api/v3";
            var apiInstance = new StudentApi(Configuration.Default);
            var student = new Student(); // Student | Update an existent student

            try
            {
                // Update an existing student
                Student result = apiInstance.UpdateStudent(student);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling StudentApi.UpdateStudent: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **student** | [**Student**](Student.md)| Update an existent student | 

### Return type

[**Student**](Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Invalid ID supplied |  -  |
| **404** | Student not found |  -  |
| **405** | Validation exception |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

