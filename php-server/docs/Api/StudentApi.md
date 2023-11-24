# OpenAPI\Client\StudentApi

All URIs are relative to https://petstore3.swagger.io/api/v3, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addStudent()**](StudentApi.md#addStudent) | **POST** /student | Add a new student |
| [**deleteStudent()**](StudentApi.md#deleteStudent) | **DELETE** /student/{studentId} | Deletes a student |
| [**getStudent()**](StudentApi.md#getStudent) | **GET** /student/{studentId} | Find student by ID |
| [**getStudentList()**](StudentApi.md#getStudentList) | **GET** /student | Get list of all students |
| [**updateStudent()**](StudentApi.md#updateStudent) | **PUT** /student | Update an existing student |


## `addStudent()`

```php
addStudent($student): \OpenAPI\Client\Model\Student
```

Add a new student

Add a new student

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\StudentApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$student = new \OpenAPI\Client\Model\Student(); // \OpenAPI\Client\Model\Student | Create a new student

try {
    $result = $apiInstance->addStudent($student);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling StudentApi->addStudent: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **student** | [**\OpenAPI\Client\Model\Student**](../Model/Student.md)| Create a new student | |

### Return type

[**\OpenAPI\Client\Model\Student**](../Model/Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`, `application/xml`, `application/x-www-form-urlencoded`
- **Accept**: `application/json`, `application/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteStudent()`

```php
deleteStudent($student_id): \OpenAPI\Client\Model\Student
```

Deletes a student

delete a student

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\StudentApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$student_id = 56; // int | Student id to delete

try {
    $result = $apiInstance->deleteStudent($student_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling StudentApi->deleteStudent: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **student_id** | **int**| Student id to delete | |

### Return type

[**\OpenAPI\Client\Model\Student**](../Model/Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getStudent()`

```php
getStudent($student_id): \OpenAPI\Client\Model\Student
```

Find student by ID

Returns a single student

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\StudentApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$student_id = 56; // int | ID of student to return

try {
    $result = $apiInstance->getStudent($student_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling StudentApi->getStudent: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **student_id** | **int**| ID of student to return | |

### Return type

[**\OpenAPI\Client\Model\Student**](../Model/Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getStudentList()`

```php
getStudentList(): \OpenAPI\Client\Model\Student[]
```

Get list of all students

Returns list of students

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\StudentApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->getStudentList();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling StudentApi->getStudentList: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\OpenAPI\Client\Model\Student[]**](../Model/Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateStudent()`

```php
updateStudent($student): \OpenAPI\Client\Model\Student
```

Update an existing student

Update an existing student by Id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\StudentApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$student = new \OpenAPI\Client\Model\Student(); // \OpenAPI\Client\Model\Student | Update an existent student

try {
    $result = $apiInstance->updateStudent($student);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling StudentApi->updateStudent: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **student** | [**\OpenAPI\Client\Model\Student**](../Model/Student.md)| Update an existent student | |

### Return type

[**\OpenAPI\Client\Model\Student**](../Model/Student.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`, `application/xml`, `application/x-www-form-urlencoded`
- **Accept**: `application/json`, `application/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
