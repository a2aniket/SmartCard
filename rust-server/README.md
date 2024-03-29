# Rust API client for openapi

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)


## Overview

This API client was generated by the [OpenAPI Generator](https://openapi-generator.tech) project.  By using the [openapi-spec](https://openapis.org) from a remote server, you can easily generate an API client.

- API version: 1.0.11
- Package version: 1.0.11
- Build package: `org.openapitools.codegen.languages.RustClientCodegen`

## Installation

Put the package under your project folder in a directory named `openapi` and add the following to `Cargo.toml` under `[dependencies]`:

```
openapi = { path = "./openapi" }
```

## Documentation for API Endpoints

All URIs are relative to *https://petstore3.swagger.io/api/v3*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CourseApi* | [**add_course**](docs/CourseApi.md#add_course) | **POST** /course | Add a new course
*CourseApi* | [**delete_course**](docs/CourseApi.md#delete_course) | **DELETE** /course/{courseId} | Deletes a course
*CourseApi* | [**get_course**](docs/CourseApi.md#get_course) | **GET** /course/{courseId} | Find course by ID
*CourseApi* | [**get_course_list**](docs/CourseApi.md#get_course_list) | **GET** /course | Get list of all courses
*CourseApi* | [**update_course**](docs/CourseApi.md#update_course) | **PUT** /course | Update an existing course
*StudentApi* | [**add_student**](docs/StudentApi.md#add_student) | **POST** /student | Add a new student
*StudentApi* | [**delete_student**](docs/StudentApi.md#delete_student) | **DELETE** /student/{studentId} | Deletes a student
*StudentApi* | [**get_student**](docs/StudentApi.md#get_student) | **GET** /student/{studentId} | Find student by ID
*StudentApi* | [**get_student_list**](docs/StudentApi.md#get_student_list) | **GET** /student | Get list of all students
*StudentApi* | [**update_student**](docs/StudentApi.md#update_student) | **PUT** /student | Update an existing student


## Documentation For Models

 - [Course](docs/Course.md)
 - [Student](docs/Student.md)


To get access to the crate's generated documentation, use:

```
cargo doc --open
```

## Author



