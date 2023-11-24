#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "student.h"



student_t *student_create(
    long id,
    char *name,
    char *address,
    char *email,
    char *phone
    ) {
    student_t *student_local_var = malloc(sizeof(student_t));
    if (!student_local_var) {
        return NULL;
    }
    student_local_var->id = id;
    student_local_var->name = name;
    student_local_var->address = address;
    student_local_var->email = email;
    student_local_var->phone = phone;

    return student_local_var;
}


void student_free(student_t *student) {
    if(NULL == student){
        return ;
    }
    listEntry_t *listEntry;
    if (student->name) {
        free(student->name);
        student->name = NULL;
    }
    if (student->address) {
        free(student->address);
        student->address = NULL;
    }
    if (student->email) {
        free(student->email);
        student->email = NULL;
    }
    if (student->phone) {
        free(student->phone);
        student->phone = NULL;
    }
    free(student);
}

cJSON *student_convertToJSON(student_t *student) {
    cJSON *item = cJSON_CreateObject();

    // student->id
    if(student->id) {
    if(cJSON_AddNumberToObject(item, "id", student->id) == NULL) {
    goto fail; //Numeric
    }
    }


    // student->name
    if(student->name) {
    if(cJSON_AddStringToObject(item, "name", student->name) == NULL) {
    goto fail; //String
    }
    }


    // student->address
    if(student->address) {
    if(cJSON_AddStringToObject(item, "address", student->address) == NULL) {
    goto fail; //String
    }
    }


    // student->email
    if(student->email) {
    if(cJSON_AddStringToObject(item, "email", student->email) == NULL) {
    goto fail; //String
    }
    }


    // student->phone
    if(student->phone) {
    if(cJSON_AddStringToObject(item, "phone", student->phone) == NULL) {
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

student_t *student_parseFromJSON(cJSON *studentJSON){

    student_t *student_local_var = NULL;

    // student->id
    cJSON *id = cJSON_GetObjectItemCaseSensitive(studentJSON, "id");
    if (id) { 
    if(!cJSON_IsNumber(id))
    {
    goto end; //Numeric
    }
    }

    // student->name
    cJSON *name = cJSON_GetObjectItemCaseSensitive(studentJSON, "name");
    if (name) { 
    if(!cJSON_IsString(name) && !cJSON_IsNull(name))
    {
    goto end; //String
    }
    }

    // student->address
    cJSON *address = cJSON_GetObjectItemCaseSensitive(studentJSON, "address");
    if (address) { 
    if(!cJSON_IsString(address) && !cJSON_IsNull(address))
    {
    goto end; //String
    }
    }

    // student->email
    cJSON *email = cJSON_GetObjectItemCaseSensitive(studentJSON, "email");
    if (email) { 
    if(!cJSON_IsString(email) && !cJSON_IsNull(email))
    {
    goto end; //String
    }
    }

    // student->phone
    cJSON *phone = cJSON_GetObjectItemCaseSensitive(studentJSON, "phone");
    if (phone) { 
    if(!cJSON_IsString(phone) && !cJSON_IsNull(phone))
    {
    goto end; //String
    }
    }


    student_local_var = student_create (
        id ? id->valuedouble : 0,
        name && !cJSON_IsNull(name) ? strdup(name->valuestring) : NULL,
        address && !cJSON_IsNull(address) ? strdup(address->valuestring) : NULL,
        email && !cJSON_IsNull(email) ? strdup(email->valuestring) : NULL,
        phone && !cJSON_IsNull(phone) ? strdup(phone->valuestring) : NULL
        );

    return student_local_var;
end:
    return NULL;

}
