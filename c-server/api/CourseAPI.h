#include <stdlib.h>
#include <stdio.h>
#include "../include/apiClient.h"
#include "../include/list.h"
#include "../external/cJSON.h"
#include "../include/keyValuePair.h"
#include "../include/binary.h"
#include "../model/course.h"


// Add a new course
//
// Add a new course
//
course_t*
CourseAPI_addCourse(apiClient_t *apiClient, course_t * course );


// Deletes a course
//
// delete a course
//
course_t*
CourseAPI_deleteCourse(apiClient_t *apiClient, long courseId );


// Find course by ID
//
// Returns a single course
//
course_t*
CourseAPI_getCourse(apiClient_t *apiClient, long courseId );


// Get list of all courses
//
// Returns list of courses
//
list_t*
CourseAPI_getCourseList(apiClient_t *apiClient);


// Update an existing course
//
// Update an existing course by Id
//
course_t*
CourseAPI_updateCourse(apiClient_t *apiClient, course_t * course );


