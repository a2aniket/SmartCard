from python-flask-server.openapi_server.controllers.student_controller import *
import unittest
from openapi_server.services.student_service import StudentService
from openapi_server.config_test import app

class TestStudentService(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_add_student(self):
        # test adding student
        response = self.app.post('/api/v3/student', json={
            'id': 1,
            'name': 'John Doe',
            'age': 20
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_student(self):
        # test deleting student
        response = self.app.delete('/api/v3/student/1')
        self.assertEqual(response.status_code, 200)

    def test_get_student(self):
        # test getting student
        response = self.app.get('/api/v3/student/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, StudentService.get_student(1))

    def test_get_student_list(self):
        # test getting list of students
        response = self.app.get('/api/v3/student')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, StudentService.get_student_list())

    def test_update_student(self):
        # test updating student
        response = self.app.put('/api/v3/student', json={
            'id': 1,
            'name': 'John Doe',
            'age': 21
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, StudentService.update_student({
            'id': 1,
            'name': 'John Doe',
            'age': 21
        }))