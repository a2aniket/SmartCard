# swagger_student_management_system_open_api_3_0

SwaggerStudentManagementSystemOpenApi30 - JavaScript client for swagger_student_management_system_open_api_3_0
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.11
- Package version: 1.0.11
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install swagger_student_management_system_open_api_3_0 --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your swagger_student_management_system_open_api_3_0 from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/YOUR_USERNAME/swagger_student_management_system_open_api_3_0
then install it via:

```shell
    npm install YOUR_USERNAME/swagger_student_management_system_open_api_3_0 --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var SwaggerStudentManagementSystemOpenApi30 = require('swagger_student_management_system_open_api_3_0');


var api = new SwaggerStudentManagementSystemOpenApi30.CourseApi()
var course = new SwaggerStudentManagementSystemOpenApi30.Course(); // {Course} Create a new course
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.addCourse(course, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://petstore3.swagger.io/api/v3*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SwaggerStudentManagementSystemOpenApi30.CourseApi* | [**addCourse**](docs/CourseApi.md#addCourse) | **POST** /course | Add a new course
*SwaggerStudentManagementSystemOpenApi30.CourseApi* | [**deleteCourse**](docs/CourseApi.md#deleteCourse) | **DELETE** /course/{courseId} | Deletes a course
*SwaggerStudentManagementSystemOpenApi30.CourseApi* | [**getCourse**](docs/CourseApi.md#getCourse) | **GET** /course/{courseId} | Find course by ID
*SwaggerStudentManagementSystemOpenApi30.CourseApi* | [**getCourseList**](docs/CourseApi.md#getCourseList) | **GET** /course | Get list of all courses
*SwaggerStudentManagementSystemOpenApi30.CourseApi* | [**updateCourse**](docs/CourseApi.md#updateCourse) | **PUT** /course | Update an existing course
*SwaggerStudentManagementSystemOpenApi30.StudentApi* | [**addStudent**](docs/StudentApi.md#addStudent) | **POST** /student | Add a new student
*SwaggerStudentManagementSystemOpenApi30.StudentApi* | [**deleteStudent**](docs/StudentApi.md#deleteStudent) | **DELETE** /student/{studentId} | Deletes a student
*SwaggerStudentManagementSystemOpenApi30.StudentApi* | [**getStudent**](docs/StudentApi.md#getStudent) | **GET** /student/{studentId} | Find student by ID
*SwaggerStudentManagementSystemOpenApi30.StudentApi* | [**getStudentList**](docs/StudentApi.md#getStudentList) | **GET** /student | Get list of all students
*SwaggerStudentManagementSystemOpenApi30.StudentApi* | [**updateStudent**](docs/StudentApi.md#updateStudent) | **PUT** /student | Update an existing student


## Documentation for Models

 - [SwaggerStudentManagementSystemOpenApi30.Course](docs/Course.md)
 - [SwaggerStudentManagementSystemOpenApi30.Student](docs/Student.md)


## Documentation for Authorization

All endpoints do not require authorization.