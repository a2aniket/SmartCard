/*
 * student.h
 *
 * 
 */

#ifndef _student_H_
#define _student_H_

#include <string.h>
#include "../external/cJSON.h"
#include "../include/list.h"
#include "../include/keyValuePair.h"
#include "../include/binary.h"

typedef struct student_t student_t;




typedef struct student_t {
    long id; //numeric
    char *name; // string
    char *address; // string
    char *email; // string
    char *phone; // string

} student_t;

student_t *student_create(
    long id,
    char *name,
    char *address,
    char *email,
    char *phone
);

void student_free(student_t *student);

student_t *student_parseFromJSON(cJSON *studentJSON);

cJSON *student_convertToJSON(student_t *student);

#endif /* _student_H_ */

