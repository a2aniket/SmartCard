from python-flask-server.openapi_server.services.course_service import *
Please note that the below code snippet is only an example of how unit tests can be written for the given code snippet. The actual number of test cases and their implementation may vary based on the requirements and edge cases of the application.

```
import unittest
from unittest.mock import patch
from openapi_server.services.course_service import CourseService

class TestCourseService(unittest.TestCase):
    @patch('openapi_server.services.course_service.Course')
    @patch('openapi_server.services.course_service.Courses_schema.dump')
    @patch('openapi_server.services.course_service.pagination_sorting')
    def test_get_course_list_empty(self, mock_pagination_sorting, mock_courses_schema_dump, mock_course):
        mock_pagination_sorting.return_value = []
        mock_courses_schema_dump.return_value = []
        result = CourseService.get_course_list()
        self.assertEqual(result, [])
    
    @patch('openapi_server.services.course_service.Course')
    @patch('openapi_server.services.course_service.Courses_schema.dump')
    @patch('openapi_server.services.course_service.pagination_sorting')
    def test_get_course_list(self, mock_pagination_sorting, mock_courses_schema_dump, mock_course):
        mock_pagination_sorting.return_value = [mock_course]
        mock_courses_schema_dump.return_value = [{}]
        result = CourseService.get_course_list()
        self.assertEqual(result, [{}])
    
    @patch('openapi_server.services.course_service.Course')
    @patch('openapi_server.services.course_service.Course_schema.dump')
    def test_get_course(self, mock_course_schema_dump, mock_course):
        mock_course.query.filter.return_value.one_or_none.return_value = mock_course
        mock_course_schema_dump.return_value = {}
        result = CourseService.get_course(1)
        self.assertEqual(result, {})
    
    @patch('openapi_server.services.course_service.Course')
    def test_get_course_invalid_id(self, mock_course):
        with self.assertRaises(Exception) as context:
            CourseService.get_course(-1)
        self.assertEqual(context.exception.code, 404)
    
    @patch('openapi_server.services.course_service.Course')
    def test_get_course_not_found(self, mock_course):
        mock_course.query.filter.return_value.one_or_none.return_value = None
        with self.assertRaises(Exception) as context:
            CourseService.get_course(1)
        self.assertEqual(context.exception.code, 404)

    @patch('openapi_server.services.course_service.Course')
    @patch('openapi_server.services.course_service.Course_schema.load')
    def test_add_course(self, mock_course_schema_load, mock_course):
        mock_course.get.return_value = 1
        mock_course.query.filter.return_value.one_or_none.return_value = None
        mock_course_schema_load.return_value = mock_course
        result = CourseService.add_course({})
        self.assertEqual(result, {})
    
    @patch('openapi_server.services.course_service.Course')
    def test_add_course_already_exists(self, mock_course):
        mock_course.get.return_value = 1
        mock_course.query.filter.return_value.one_or_none.return_value = mock_course
        with self.assertRaises(Exception) as context:
            CourseService.add_course({})
        self.assertEqual(context.exception.code, 400)
    
    @patch('openapi_server.services.course_service.Course')
    @patch('openapi_server.services.course_service.Course_schema.load')
    def test_update_course(self, mock_course_schema_load, mock_course):
        mock_course.get.return_value = 1
        mock_course.query.filter.return_value.one_or_none.return_value = mock_course
        mock_course_schema_load.return_value = mock_course
        result = CourseService.update_course({})
        self.assertEqual(result, {})
    
    @patch('openapi_server.services.course_service.Course')
    def test_update_course_not_found(self, mock_course):
        mock_course.query.filter.return_value.one_or_none.return_value = None
        with self.assertRaises(Exception) as context:
            CourseService.update_course({})
        self.assertEqual(context.exception.code, 404)
    
    @patch('openapi_server.services.course_service.Course')
    def test_delete_course(self, mock_course):
        mock_course.query.filter.return_value.one_or_none.return_value = mock_course
        result = CourseService.delete_course(1)
        self.assertEqual(result, 'Course with ID: 1 successfully deleted')
    
    @patch('openapi_server.services.course_service.Course')
    def test_delete_course_not_found(self, mock_course):
        mock_course.query.filter.return_value.one_or_none.return_value = None
        with self.assertRaises(Exception) as context:
            CourseService.delete_course(1)
        self.assertEqual(context.exception.code, 400)