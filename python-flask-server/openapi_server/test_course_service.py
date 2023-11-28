from services.course_service import *
import unittest
from unittest.mock import patch, MagicMock
from openapi_server.services.course_service import CourseService

class TestCourseService(unittest.TestCase):

    @patch('openapi_server.services.course_service.pagination_sorting')
    def test_get_course_list(self, mock_pagination_sorting):
        # Test case for successful retrieval of courses
        mock_pagination_sorting.return_value = [{'id': 1, 'name': 'Course 1'}, {'id': 2, 'name': 'Course 2'}]
        result = CourseService.get_course_list()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['id'], 1)
        self.assertEqual(result[0]['name'], 'Course 1')
        self.assertEqual(result[1]['id'], 2)
        self.assertEqual(result[1]['name'], 'Course 2')

        # Test case for no courses found
        mock_pagination_sorting.return_value = []
        with self.assertRaises(Exception):
            CourseService.get_course_list()

    @patch('openapi_server.services.course_service.Course.query')
    def test_get_course(self, mock_course_query):
        # Test case for successful retrieval of course by ID
        mock_course_query.filter().one_or_none.return_value = {'id': 1, 'name': 'Course 1'}
        result = CourseService.get_course(1)
        self.assertEqual(result['id'], 1)
        self.assertEqual(result['name'], 'Course 1')

        # Test case for course not found
        mock_course_query.filter().one_or_none.return_value = None
        with self.assertRaises(Exception):
            CourseService.get_course(1)

        # Test case for invalid ID
        with self.assertRaises(Exception):
            CourseService.get_course(-1)

    @patch('openapi_server.services.course_service.Course.query')
    def test_add_course(self, mock_course_query):
        # Test case for successful addition of new course
        mock_course_query.filter().one_or_none.return_value = None
        mock_course = MagicMock()
        mock_course.get.return_value = 1
        mock_course_load = MagicMock()
        mock_course_load.return_value = mock_course
        with patch('openapi_server.services.course_service.Course_schema.load', mock_course_load):
            result = CourseService.add_course({'id': 1, 'name': 'Course 1'})
        self.assertEqual(result['id'], 1)
        self.assertEqual(result['name'], 'Course 1')

        # Test case for course with same ID already exists
        mock_course_query.filter().one_or_none.return_value = {'id': 1, 'name': 'Course 1'}
        with self.assertRaises(Exception):
            CourseService.add_course({'id': 1, 'name': 'Course 1'})

    @patch('openapi_server.services.course_service.Course.query')
    def test_update_course(self, mock_course_query):
        # Test case for successful update of existing course
        mock_course_query.filter().one_or_none.return_value = {'id': 1, 'name': 'Course 1'}
        mock_course = MagicMock()
        mock_course.get.return_value = 1
        mock_course_load = MagicMock()
        mock_course_load.return_value = mock_course
        with patch('openapi_server.services.course_service.Course_schema.load', mock_course_load):
            result = CourseService.update_course({'id': 1, 'name': 'Course 2'})
        self.assertEqual(result['id'], 1)
        self.assertEqual(result['name'], 'Course 2')

        # Test case for course not found
        mock_course_query.filter().one_or_none.return_value = None
        with self.assertRaises(Exception):
            CourseService.update_course({'id': 1, 'name': 'Course 2'})

    @patch('openapi_server.services.course_service.Course.query')
    def test_delete_course(self, mock_course_query):
        # Test case for successful deletion of course
        mock_course_query.filter().one_or_none.return_value = {'id': 1, 'name': 'Course 1'}
        result = CourseService.delete_course(1)
        self.assertEqual(result, 'Course with ID: 1 successfully deleted')

        # Test case for course not found
        mock_course_query.filter().one_or_none.return_value = None
        with self.assertRaises(Exception):
            CourseService.delete_course(1)