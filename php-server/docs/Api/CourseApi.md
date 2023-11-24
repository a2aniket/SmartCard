# OpenAPI\Client\CourseApi

All URIs are relative to https://petstore3.swagger.io/api/v3, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addCourse()**](CourseApi.md#addCourse) | **POST** /course | Add a new course |
| [**deleteCourse()**](CourseApi.md#deleteCourse) | **DELETE** /course/{courseId} | Deletes a course |
| [**getCourse()**](CourseApi.md#getCourse) | **GET** /course/{courseId} | Find course by ID |
| [**getCourseList()**](CourseApi.md#getCourseList) | **GET** /course | Get list of all courses |
| [**updateCourse()**](CourseApi.md#updateCourse) | **PUT** /course | Update an existing course |


## `addCourse()`

```php
addCourse($course): \OpenAPI\Client\Model\Course
```

Add a new course

Add a new course

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\CourseApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$course = new \OpenAPI\Client\Model\Course(); // \OpenAPI\Client\Model\Course | Create a new course

try {
    $result = $apiInstance->addCourse($course);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CourseApi->addCourse: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **course** | [**\OpenAPI\Client\Model\Course**](../Model/Course.md)| Create a new course | |

### Return type

[**\OpenAPI\Client\Model\Course**](../Model/Course.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`, `application/xml`, `application/x-www-form-urlencoded`
- **Accept**: `application/json`, `application/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteCourse()`

```php
deleteCourse($course_id): \OpenAPI\Client\Model\Course
```

Deletes a course

delete a course

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\CourseApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$course_id = 56; // int | Course id to delete

try {
    $result = $apiInstance->deleteCourse($course_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CourseApi->deleteCourse: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **course_id** | **int**| Course id to delete | |

### Return type

[**\OpenAPI\Client\Model\Course**](../Model/Course.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCourse()`

```php
getCourse($course_id): \OpenAPI\Client\Model\Course
```

Find course by ID

Returns a single course

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\CourseApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$course_id = 56; // int | ID of course to return

try {
    $result = $apiInstance->getCourse($course_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CourseApi->getCourse: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **course_id** | **int**| ID of course to return | |

### Return type

[**\OpenAPI\Client\Model\Course**](../Model/Course.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCourseList()`

```php
getCourseList(): \OpenAPI\Client\Model\Course[]
```

Get list of all courses

Returns list of courses

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\CourseApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->getCourseList();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CourseApi->getCourseList: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\OpenAPI\Client\Model\Course[]**](../Model/Course.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateCourse()`

```php
updateCourse($course): \OpenAPI\Client\Model\Course
```

Update an existing course

Update an existing course by Id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\CourseApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$course = new \OpenAPI\Client\Model\Course(); // \OpenAPI\Client\Model\Course | Update an existent course

try {
    $result = $apiInstance->updateCourse($course);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CourseApi->updateCourse: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **course** | [**\OpenAPI\Client\Model\Course**](../Model/Course.md)| Update an existent course | |

### Return type

[**\OpenAPI\Client\Model\Course**](../Model/Course.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`, `application/xml`, `application/x-www-form-urlencoded`
- **Accept**: `application/json`, `application/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
