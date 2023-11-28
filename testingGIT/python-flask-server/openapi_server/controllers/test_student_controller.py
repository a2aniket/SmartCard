from student_controller import *
import unittest
import json
from openapi_server.config_test import app

class TestStudentService(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_add_student(self):
        # Test adding a student
        student = {'name': 'John', 'age': 21}
        response = self.client.post('/api/v3/student', json=student)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['success'])

    def test_delete_student(self):
        # Test deleting a student
        student_id = '1'
        response = self.client.delete(f'/api/v3/student/{student_id}')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['success'])

    def test_get_student(self):
        # Test getting a student
        student_id = '1'
        response = self.client.get(f'/api/v3/student/{student_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json)

    def test_get_student_list(self):
        # Test getting a list of students
        response = self.client.get('/api/v3/student')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json)

    def test_update_student(self):
        # Test updating a student
        student = {'id': '1', 'name': 'John Doe', 'age': 22}
        response = self.client.put('/api/v3/student', json=student)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['success'])