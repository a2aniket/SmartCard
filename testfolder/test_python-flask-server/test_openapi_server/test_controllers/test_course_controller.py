from python-flask-server.openapi_server.controllers.course_controller import *
import unittest
from unittest.mock import patch
import json

from openapi_server import app
from openapi_server.services.course_service import CourseService


class TestCourseService(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_add_course(self):
        # Test adding a new course
        with patch.object(CourseService, 'add_course', return_value={"id": 1, "name": "Test Course"}) as mock_add_course:
            response = self.app.post('/api/v3/course', json={"name": "Test Course"})
            mock_add_course.assert_called_once_with({"name": "Test Course"})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data), {"id": 1, "name": "Test Course"})

    def test_delete_course(self):
        # Test deleting a course
        with patch.object(CourseService, 'delete_course', return_value={"id": 1, "name": "Test Course"}) as mock_delete_course:
            response = self.app.delete('/api/v3/course/1')
            mock_delete_course.assert_called_once_with(1)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data), {"id": 1, "name": "Test Course"})

    def test_get_course(self):
        # Test getting a course
        with patch.object(CourseService, 'get_course', return_value={"id": 1, "name": "Test Course"}) as mock_get_course:
            response = self.app.get('/api/v3/course/1')
            mock_get_course.assert_called_once_with(1)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data), {"id": 1, "name": "Test Course"})

    def test_get_course_list(self):
        # Test getting a list of courses
        with patch.object(CourseService, 'get_course_list', return_value=[{"id": 1, "name": "Test Course"}]) as mock_get_course_list:
            response = self.app.get('/api/v3/course')
            mock_get_course_list.assert_called_once()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data), [{"id": 1, "name": "Test Course"}])

    def test_update_course(self):
        # Test updating a course
        with patch.object(CourseService, 'update_course', return_value={"id": 1, "name": "Updated Test Course"}) as mock_update_course:
            response = self.app.put('/api/v3/course', json={"id": 1, "name": "Updated Test Course"})
            mock_update_course.assert_called_once_with({"id": 1, "name": "Updated Test Course"})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data), {"id": 1, "name": "Updated Test Course"})