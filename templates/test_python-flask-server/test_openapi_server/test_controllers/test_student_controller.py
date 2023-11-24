from python-flask-server.openapi_server.controllers.student_controller import *
import unittest
import json
from openapi_server.config_test import app


class TestStudentService(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.student = {
            "name": "John Doe",
            "age": 22,
            "gender": "Male",
            "class": "A"
        }
        self.updated_student = {
            "name": "Jane Doe",
            "age": 23,
            "gender": "Female",
            "class": "B"
        }

    def test_add_student(self):
        response = self.client.post('/api/v3/student', json=self.student)
        self.assertEqual(response.status_code, 200)

    def test_delete_student(self):
        response = self.client.post('/api/v3/student', json=self.student)
        student_id = json.loads(response.data)['id']
        response = self.client.delete(f'/api/v3/student/{student_id}')
        self.assertEqual(response.status_code, 200)

    def test_get_student(self):
        response = self.client.post('/api/v3/student', json=self.student)
        student_id = json.loads(response.data)['id']
        response = self.client.get(f'/api/v3/student/{student_id}')
        self.assertEqual(response.status_code, 200)

    def test_get_student_list(self):
        response = self.client.get('/api/v3/student')
        self.assertEqual(response.status_code, 200)

    def test_update_student(self):
        response = self.client.post('/api/v3/student', json=self.student)
        student_id = json.loads(response.data)['id']
        response = self.client.put(f'/api/v3/student/{student_id}', json=self.updated_student)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()