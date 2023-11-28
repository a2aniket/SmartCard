from course_controller import *
import unittest
from unittest.mock import MagicMock
from openapi_server import app
from openapi_server.services.course_service import CourseService


class TestCourseService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add_course(self):
        # Test adding new course
        course = {'course_id': 1, 'name': 'Maths', 'description': 'Mathematics'}
        response = self.app.post('/api/v3/course', json=course)
        self.assertEqual(response.status_code, 200)

        # Test adding duplicate course
        response = self.app.post('/api/v3/course', json=course)
        self.assertEqual(response.status_code, 409)

    def test_delete_course(self):
        # Test deleting existing course
        response = self.app.delete('/api/v3/course/1')
        self.assertEqual(response.status_code, 200)

        # Test deleting non-existing course
        response = self.app.delete('/api/v3/course/1')
        self.assertEqual(response.status_code, 404)

    def test_get_course(self):
        # Test getting existing course
        response = self.app.get('/api/v3/course/1')
        self.assertEqual(response.status_code, 200)

        # Test getting non-existing course
        response = self.app.get('/api/v3/course/2')
        self.assertEqual(response.status_code, 404)

    def test_get_course_list(self):
        # Test getting course list
        response = self.app.get('/api/v3/course')
        self.assertEqual(response.status_code, 200)

    def test_update_course(self):
        # Test updating existing course
        course = {'course_id': 1, 'name': 'Maths', 'description': 'Mathematics'}
        response = self.app.put('/api/v3/course', json=course)
        self.assertEqual(response.status_code, 200)

        # Test updating non-existing course
        course = {'course_id': 2, 'name': 'Science', 'description': 'Science'}
        response = self.app.put('/api/v3/course', json=course)
        self.assertEqual(response.status_code, 404)