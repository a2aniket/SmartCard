from python-flask-server.openapi_server.controllers.course_controller import *
import unittest
from unittest.mock import MagicMock
from openapi_server.services.course_service import CourseService
from openapi_server.config_test import app


class TestCourseService(unittest.TestCase):

    def test_add_course(self):
        app.config['TESTING'] = True
        with app.test_client() as client:
            course = {
                "name": "Math",
                "description": "Mathematics"
            }
            response = client.post('/api/v3/course', json=course)
            self.assertEqual(response.status_code, 200)

    def test_delete_course(self):
        app.config['TESTING'] = True
        with app.test_client() as client:
            course_id = 1
            response = client.delete(f'/api/v3/course/{course_id}')
            self.assertEqual(response.status_code, 200)

    def test_get_course(self):
        app.config['TESTING'] = True
        with app.test_client() as client:
            course_id = 1
            response = client.get(f'/api/v3/course/{course_id}')
            self.assertEqual(response.status_code, 200)

    def test_get_course_list(self):
        app.config['TESTING'] = True
        with app.test_client() as client:
            response = client.get('/api/v3/course')
            self.assertEqual(response.status_code, 200)

    def test_update_course(self):
        app.config['TESTING'] = True
        with app.test_client() as client:
            course = {
                "id": 1,
                "name": "Math",
                "description": "Mathematics"
            }
            response = client.put('/api/v3/course', json=course)
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()