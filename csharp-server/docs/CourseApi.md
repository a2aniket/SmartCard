# Org.OpenAPITools.Api.CourseApi

All URIs are relative to *https://petstore3.swagger.io/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddCourse**](CourseApi.md#addcourse) | **POST** /course | Add a new course
[**DeleteCourse**](CourseApi.md#deletecourse) | **DELETE** /course/{courseId} | Deletes a course
[**GetCourse**](CourseApi.md#getcourse) | **GET** /course/{courseId} | Find course by ID
[**GetCourseList**](CourseApi.md#getcourselist) | **GET** /course | Get list of all courses
[**UpdateCourse**](CourseApi.md#updatecourse) | **PUT** /course | Update an existing course



## AddCourse

> Course AddCourse (Course course)

Add a new course

Add a new course

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class AddCourseExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "https://petstore3.swagger.io/api/v3";
            var apiInstance = new CourseApi(Configuration.Default);
            var course = new Course(); // Course | Create a new course

            try
            {
                // Add a new course
                Course result = apiInstance.AddCourse(course);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling CourseApi.AddCourse: " + e.Message );
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
 **course** | [**Course**](Course.md)| Create a new course | 

### Return type

[**Course**](Course.md)

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


## DeleteCourse

> Course DeleteCourse (long courseId)

Deletes a course

delete a course

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class DeleteCourseExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "https://petstore3.swagger.io/api/v3";
            var apiInstance = new CourseApi(Configuration.Default);
            var courseId = 789L;  // long | Course id to delete

            try
            {
                // Deletes a course
                Course result = apiInstance.DeleteCourse(courseId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling CourseApi.DeleteCourse: " + e.Message );
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
 **courseId** | **long**| Course id to delete | 

### Return type

[**Course**](Course.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid course value |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetCourse

> Course GetCourse (long courseId)

Find course by ID

Returns a single course

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class GetCourseExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "https://petstore3.swagger.io/api/v3";
            var apiInstance = new CourseApi(Configuration.Default);
            var courseId = 789L;  // long | ID of course to return

            try
            {
                // Find course by ID
                Course result = apiInstance.GetCourse(courseId);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling CourseApi.GetCourse: " + e.Message );
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
 **courseId** | **long**| ID of course to return | 

### Return type

[**Course**](Course.md)

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
| **404** | Course not found |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetCourseList

> List&lt;Course&gt; GetCourseList ()

Get list of all courses

Returns list of courses

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class GetCourseListExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "https://petstore3.swagger.io/api/v3";
            var apiInstance = new CourseApi(Configuration.Default);

            try
            {
                // Get list of all courses
                List<Course> result = apiInstance.GetCourseList();
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling CourseApi.GetCourseList: " + e.Message );
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

[**List&lt;Course&gt;**](Course.md)

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
| **404** | Course not found |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateCourse

> Course UpdateCourse (Course course)

Update an existing course

Update an existing course by Id

### Example

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class UpdateCourseExample
    {
        public static void Main()
        {
            Configuration.Default.BasePath = "https://petstore3.swagger.io/api/v3";
            var apiInstance = new CourseApi(Configuration.Default);
            var course = new Course(); // Course | Update an existent course

            try
            {
                // Update an existing course
                Course result = apiInstance.UpdateCourse(course);
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling CourseApi.UpdateCourse: " + e.Message );
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
 **course** | [**Course**](Course.md)| Update an existent course | 

### Return type

[**Course**](Course.md)

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
| **404** | Course not found |  -  |
| **405** | Validation exception |  -  |

[[Back to top]](#)
[[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

