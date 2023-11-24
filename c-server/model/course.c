#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "course.h"



course_t *course_create(
    long id,
    char *name,
    char *desc
    ) {
    course_t *course_local_var = malloc(sizeof(course_t));
    if (!course_local_var) {
        return NULL;
    }
    course_local_var->id = id;
    course_local_var->name = name;
    course_local_var->desc = desc;

    return course_local_var;
}


void course_free(course_t *course) {
    if(NULL == course){
        return ;
    }
    listEntry_t *listEntry;
    if (course->name) {
        free(course->name);
        course->name = NULL;
    }
    if (course->desc) {
        free(course->desc);
        course->desc = NULL;
    }
    free(course);
}

cJSON *course_convertToJSON(course_t *course) {
    cJSON *item = cJSON_CreateObject();

    // course->id
    if(course->id) {
    if(cJSON_AddNumberToObject(item, "id", course->id) == NULL) {
    goto fail; //Numeric
    }
    }


    // course->name
    if(course->name) {
    if(cJSON_AddStringToObject(item, "name", course->name) == NULL) {
    goto fail; //String
    }
    }


    // course->desc
    if(course->desc) {
    if(cJSON_AddStringToObject(item, "desc", course->desc) == NULL) {
    goto fail; //String
    }
    }

    return item;
fail:
    if (item) {
        cJSON_Delete(item);
    }
    return NULL;
}

course_t *course_parseFromJSON(cJSON *courseJSON){

    course_t *course_local_var = NULL;

    // course->id
    cJSON *id = cJSON_GetObjectItemCaseSensitive(courseJSON, "id");
    if (id) { 
    if(!cJSON_IsNumber(id))
    {
    goto end; //Numeric
    }
    }

    // course->name
    cJSON *name = cJSON_GetObjectItemCaseSensitive(courseJSON, "name");
    if (name) { 
    if(!cJSON_IsString(name) && !cJSON_IsNull(name))
    {
    goto end; //String
    }
    }

    // course->desc
    cJSON *desc = cJSON_GetObjectItemCaseSensitive(courseJSON, "desc");
    if (desc) { 
    if(!cJSON_IsString(desc) && !cJSON_IsNull(desc))
    {
    goto end; //String
    }
    }


    course_local_var = course_create (
        id ? id->valuedouble : 0,
        name && !cJSON_IsNull(name) ? strdup(name->valuestring) : NULL,
        desc && !cJSON_IsNull(desc) ? strdup(desc->valuestring) : NULL
        );

    return course_local_var;
end:
    return NULL;

}
