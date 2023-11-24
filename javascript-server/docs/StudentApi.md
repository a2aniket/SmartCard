# SwaggerStudentManagementSystemOpenApi30.StudentApi

All URIs are relative to *https://petstore3.swagger.io/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addStudent**](StudentApi.md#addStudent) | **POST** /student | Add a new student
[**deleteStudent**](StudentApi.md#deleteStudent) | **DELETE** /student/{studentId} | Deletes a student
[**getStudent**](StudentApi.md#getStudent) | **GET** /student/{studentId} | Find student by ID
[**getStudentList**](StudentApi.md#getStudentList) | **GET** /student | Get list of all students
[**updateStudent**](StudentApi.md#updateStudent) | **PUT** /student | Update an existing student



## addStudent

> Student addStudent(student)

Add a new student

Add a new student

### Example

```javascript
import SwaggerStudentManagementSystemOpenApi30 from 'swagger_student_management_system_open_api_3_0';

let apiInstance = new SwaggerStudentManagementSystemOpenApi30.StudentApi();
let student = new SwaggerStudentManagementSystemOpenApi30.Student(); // Student | Create a new student
apiInstance.addStudent(student, (error, data, response) => {
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
 **student** | [**Student**](Student.md)| Create a new student | 

### Return type

[**Student**](Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## deleteStudent

> Student deleteStudent(studentId)

Deletes a student

delete a student

### Example

```javascript
import SwaggerStudentManagementSystemOpenApi30 from 'swagger_student_management_system_open_api_3_0';

let apiInstance = new SwaggerStudentManagementSystemOpenApi30.StudentApi();
let studentId = 789; // Number | Student id to delete
apiInstance.deleteStudent(studentId, (error, data, response) => {
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
 **studentId** | **Number**| Student id to delete | 

### Return type

[**Student**](Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getStudent

> Student getStudent(studentId)

Find student by ID

Returns a single student

### Example

```javascript
import SwaggerStudentManagementSystemOpenApi30 from 'swagger_student_management_system_open_api_3_0';

let apiInstance = new SwaggerStudentManagementSystemOpenApi30.StudentApi();
let studentId = 789; // Number | ID of student to return
apiInstance.getStudent(studentId, (error, data, response) => {
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
 **studentId** | **Number**| ID of student to return | 

### Return type

[**Student**](Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getStudentList

> [Student] getStudentList()

Get list of all students

Returns list of students

### Example

```javascript
import SwaggerStudentManagementSystemOpenApi30 from 'swagger_student_management_system_open_api_3_0';

let apiInstance = new SwaggerStudentManagementSystemOpenApi30.StudentApi();
apiInstance.getStudentList((error, data, response) => {
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

[**[Student]**](Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## updateStudent

> Student updateStudent(student)

Update an existing student

Update an existing student by Id

### Example

```javascript
import SwaggerStudentManagementSystemOpenApi30 from 'swagger_student_management_system_open_api_3_0';

let apiInstance = new SwaggerStudentManagementSystemOpenApi30.StudentApi();
let student = new SwaggerStudentManagementSystemOpenApi30.Student(); // Student | Update an existent student
apiInstance.updateStudent(student, (error, data, response) => {
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
 **student** | [**Student**](Student.md)| Update an existent student | 

### Return type

[**Student**](Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
- **Accept**: application/json, application/xml

