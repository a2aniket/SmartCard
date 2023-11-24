#ifndef course_TEST
#define course_TEST

// the following is to include only the main from the first c file
#ifndef TEST_MAIN
#define TEST_MAIN
#define course_MAIN
#endif // TEST_MAIN

#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include "../external/cJSON.h"

#include "../model/course.h"
course_t* instantiate_course(int include_optional);



course_t* instantiate_course(int include_optional) {
  course_t* course = NULL;
  if (include_optional) {
    course = course_create(
      1,
      "0",
      "0"
    );
  } else {
    course = course_create(
      1,
      "0",
      "0"
    );
  }

  return course;
}


#ifdef course_MAIN

void test_course(int include_optional) {
    course_t* course_1 = instantiate_course(include_optional);

	cJSON* jsoncourse_1 = course_convertToJSON(course_1);
	printf("course :\n%s\n", cJSON_Print(jsoncourse_1));
	course_t* course_2 = course_parseFromJSON(jsoncourse_1);
	cJSON* jsoncourse_2 = course_convertToJSON(course_2);
	printf("repeating course:\n%s\n", cJSON_Print(jsoncourse_2));
}

int main() {
  test_course(1);
  test_course(0);

  printf("Hello world \n");
  return 0;
}

#endif // course_MAIN
#endif // course_TEST
