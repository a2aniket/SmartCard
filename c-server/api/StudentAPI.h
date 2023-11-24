#include <stdlib.h>
#include <stdio.h>
#include "../include/apiClient.h"
#include "../include/list.h"
#include "../external/cJSON.h"
#include "../include/keyValuePair.h"
#include "../include/binary.h"
#include "../model/student.h"


// Add a new student
//
// Add a new student
//
student_t*
StudentAPI_addStudent(apiClient_t *apiClient, student_t * student );


// Deletes a student
//
// delete a student
//
student_t*
StudentAPI_deleteStudent(apiClient_t *apiClient, long studentId );


// Find student by ID
//
// Returns a single student
//
student_t*
StudentAPI_getStudent(apiClient_t *apiClient, long studentId );


// Get list of all students
//
// Returns list of students
//
list_t*
StudentAPI_getStudentList(apiClient_t *apiClient);


// Update an existing student
//
// Update an existing student by Id
//
student_t*
StudentAPI_updateStudent(apiClient_t *apiClient, student_t * student );


