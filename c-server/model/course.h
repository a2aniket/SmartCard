/*
 * course.h
 *
 * 
 */

#ifndef _course_H_
#define _course_H_

#include <string.h>
#include "../external/cJSON.h"
#include "../include/list.h"
#include "../include/keyValuePair.h"
#include "../include/binary.h"

typedef struct course_t course_t;




typedef struct course_t {
    long id; //numeric
    char *name; // string
    char *desc; // string

} course_t;

course_t *course_create(
    long id,
    char *name,
    char *desc
);

void course_free(course_t *course);

course_t *course_parseFromJSON(cJSON *courseJSON);

cJSON *course_convertToJSON(course_t *course);

#endif /* _course_H_ */

