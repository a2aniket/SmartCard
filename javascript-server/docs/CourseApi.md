# SwaggerStudentManagementSystemOpenApi30.CourseApi

All URIs are relative to *https://petstore3.swagger.io/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addCourse**](CourseApi.md#addCourse) | **POST** /course | Add a new course
[**deleteCourse**](CourseApi.md#deleteCourse) | **DELETE** /course/{courseId} | Deletes a course
[**getCourse**](CourseApi.md#getCourse) | **GET** /course/{courseId} | Find course by ID
[**getCourseList**](CourseApi.md#getCourseList) | **GET** /course | Get list of all courses
[**updateCourse**](CourseApi.md#updateCourse) | **PUT** /course | Update an existing course



## addCourse

> Course addCourse(course)

Add a new course

Add a new course

### Example

```javascript
import SwaggerStudentManagementSystemOpenApi30 from 'swagger_student_management_system_open_api_3_0';

let apiInstance = new SwaggerStudentManagementSystemOpenApi30.CourseApi();
let course = new SwaggerStudentManagementSystemOpenApi30.Course(); // Course | Create a new course
apiInstance.addCourse(course, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## deleteCourse

> Course deleteCourse(courseId)

Deletes a course

delete a course

### Example

```javascript
import SwaggerStudentManagementSystemOpenApi30 from 'swagger_student_management_system_open_api_3_0';

let apiInstance = new SwaggerStudentManagementSystemOpenApi30.CourseApi();
let courseId = 789; // Number | Course id to delete
apiInstance.deleteCourse(courseId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **courseId** | **Number**| Course id to delete | 

### Return type

[**Course**](Course.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getCourse

> Course getCourse(courseId)

Find course by ID

Returns a single course

### Example

```javascript
import SwaggerStudentManagementSystemOpenApi30 from 'swagger_student_management_system_open_api_3_0';

let apiInstance = new SwaggerStudentManagementSystemOpenApi30.CourseApi();
let courseId = 789; // Number | ID of course to return
apiInstance.getCourse(courseId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **courseId** | **Number**| ID of course to return | 

### Return type

[**Course**](Course.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getCourseList

> [Course] getCourseList()

Get list of all courses

Returns list of courses

### Example

```javascript
import SwaggerStudentManagementSystemOpenApi30 from 'swagger_student_management_system_open_api_3_0';

let apiInstance = new SwaggerStudentManagementSystemOpenApi30.CourseApi();
apiInstance.getCourseList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Course]**](Course.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## updateCourse

> Course updateCourse(course)

Update an existing course

Update an existing course by Id

### Example

```javascript
import SwaggerStudentManagementSystemOpenApi30 from 'swagger_student_management_system_open_api_3_0';

let apiInstance = new SwaggerStudentManagementSystemOpenApi30.CourseApi();
let course = new SwaggerStudentManagementSystemOpenApi30.Course(); // Course | Update an existent course
apiInstance.updateCourse(course, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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

