# CourseApi

All URIs are relative to *https://petstore3.swagger.io/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addCourse**](CourseApi.md#addCourse) | **POST** /course | Add a new course
[**deleteCourse**](CourseApi.md#deleteCourse) | **DELETE** /course/{courseId} | Deletes a course
[**getCourse**](CourseApi.md#getCourse) | **GET** /course/{courseId} | Find course by ID
[**getCourseList**](CourseApi.md#getCourseList) | **GET** /course | Get list of all courses
[**updateCourse**](CourseApi.md#updateCourse) | **PUT** /course | Update an existing course


<a name="addCourse"></a>
# **addCourse**
> Course addCourse(course)

Add a new course

Add a new course

### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = CourseApi()
val course : Course =  // Course | Create a new course
try {
    val result : Course = apiInstance.addCourse(course)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling CourseApi#addCourse")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CourseApi#addCourse")
    e.printStackTrace()
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

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="deleteCourse"></a>
# **deleteCourse**
> Course deleteCourse(courseId)

Deletes a course

delete a course

### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = CourseApi()
val courseId : kotlin.Long = 789 // kotlin.Long | Course id to delete
try {
    val result : Course = apiInstance.deleteCourse(courseId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling CourseApi#deleteCourse")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CourseApi#deleteCourse")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **courseId** | **kotlin.Long**| Course id to delete |

### Return type

[**Course**](Course.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getCourse"></a>
# **getCourse**
> Course getCourse(courseId)

Find course by ID

Returns a single course

### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = CourseApi()
val courseId : kotlin.Long = 789 // kotlin.Long | ID of course to return
try {
    val result : Course = apiInstance.getCourse(courseId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling CourseApi#getCourse")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CourseApi#getCourse")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **courseId** | **kotlin.Long**| ID of course to return |

### Return type

[**Course**](Course.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getCourseList"></a>
# **getCourseList**
> kotlin.collections.List&lt;Course&gt; getCourseList()

Get list of all courses

Returns list of courses

### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = CourseApi()
try {
    val result : kotlin.collections.List<Course> = apiInstance.getCourseList()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling CourseApi#getCourseList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CourseApi#getCourseList")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;Course&gt;**](Course.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="updateCourse"></a>
# **updateCourse**
> Course updateCourse(course)

Update an existing course

Update an existing course by Id

### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = CourseApi()
val course : Course =  // Course | Update an existent course
try {
    val result : Course = apiInstance.updateCourse(course)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling CourseApi#updateCourse")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CourseApi#updateCourse")
    e.printStackTrace()
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

 - **Content-Type**: application/json
 - **Accept**: application/json

