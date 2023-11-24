#ifndef student_TEST
#define student_TEST

// the following is to include only the main from the first c file
#ifndef TEST_MAIN
#define TEST_MAIN
#define student_MAIN
#endif // TEST_MAIN

#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include "../external/cJSON.h"

#include "../model/student.h"
student_t* instantiate_student(int include_optional);



student_t* instantiate_student(int include_optional) {
  student_t* student = NULL;
  if (include_optional) {
    student = student_create(
      1,
      "Ramesh",
      "Pune",
      "ramesh@email.com",
      "1234567890"
    );
  } else {
    student = student_create(
      1,
      "Ramesh",
      "Pune",
      "ramesh@email.com",
      "1234567890"
    );
  }

  return student;
}


#ifdef student_MAIN

void test_student(int include_optional) {
    student_t* student_1 = instantiate_student(include_optional);

	cJSON* jsonstudent_1 = student_convertToJSON(student_1);
	printf("student :\n%s\n", cJSON_Print(jsonstudent_1));
	student_t* student_2 = student_parseFromJSON(jsonstudent_1);
	cJSON* jsonstudent_2 = student_convertToJSON(student_2);
	printf("repeating student:\n%s\n", cJSON_Print(jsonstudent_2));
}

int main() {
  test_student(1);
  test_student(0);

  printf("Hello world \n");
  return 0;
}

#endif // student_MAIN
#endif // student_TEST
