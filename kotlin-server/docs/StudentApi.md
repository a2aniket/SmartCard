# StudentApi

All URIs are relative to *https://petstore3.swagger.io/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addStudent**](StudentApi.md#addStudent) | **POST** /student | Add a new student
[**deleteStudent**](StudentApi.md#deleteStudent) | **DELETE** /student/{studentId} | Deletes a student
[**getStudent**](StudentApi.md#getStudent) | **GET** /student/{studentId} | Find student by ID
[**getStudentList**](StudentApi.md#getStudentList) | **GET** /student | Get list of all students
[**updateStudent**](StudentApi.md#updateStudent) | **PUT** /student | Update an existing student


<a name="addStudent"></a>
# **addStudent**
> Student addStudent(student)

Add a new student

Add a new student

### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = StudentApi()
val student : Student =  // Student | Create a new student
try {
    val result : Student = apiInstance.addStudent(student)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling StudentApi#addStudent")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling StudentApi#addStudent")
    e.printStackTrace()
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

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="deleteStudent"></a>
# **deleteStudent**
> Student deleteStudent(studentId)

Deletes a student

delete a student

### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = StudentApi()
val studentId : kotlin.Long = 789 // kotlin.Long | Student id to delete
try {
    val result : Student = apiInstance.deleteStudent(studentId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling StudentApi#deleteStudent")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling StudentApi#deleteStudent")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studentId** | **kotlin.Long**| Student id to delete |

### Return type

[**Student**](Student.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getStudent"></a>
# **getStudent**
> Student getStudent(studentId)

Find student by ID

Returns a single student

### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = StudentApi()
val studentId : kotlin.Long = 789 // kotlin.Long | ID of student to return
try {
    val result : Student = apiInstance.getStudent(studentId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling StudentApi#getStudent")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling StudentApi#getStudent")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studentId** | **kotlin.Long**| ID of student to return |

### Return type

[**Student**](Student.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getStudentList"></a>
# **getStudentList**
> kotlin.collections.List&lt;Student&gt; getStudentList()

Get list of all students

Returns list of students

### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = StudentApi()
try {
    val result : kotlin.collections.List<Student> = apiInstance.getStudentList()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling StudentApi#getStudentList")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling StudentApi#getStudentList")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;Student&gt;**](Student.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="updateStudent"></a>
# **updateStudent**
> Student updateStudent(student)

Update an existing student

Update an existing student by Id

### Example
```kotlin
// Import classes:
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiInstance = StudentApi()
val student : Student =  // Student | Update an existent student
try {
    val result : Student = apiInstance.updateStudent(student)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling StudentApi#updateStudent")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling StudentApi#updateStudent")
    e.printStackTrace()
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

 - **Content-Type**: application/json
 - **Accept**: application/json

