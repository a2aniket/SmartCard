from python-flask-server.openapi_server.services.student_service import *
import unittest
from openapi_server.config_test import app, db
from openapi_server.models.student import Student, Student_schema, Students_schema
from openapi_server.services.pagination_sorting import pagination_sorting

class TestStudentService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()

    def setUp(self):
        self.client = app.test_client()
        self.student1 = {"id": 1, "name": "John", "age": 21, "city": "New York"}
        self.student2 = {"id": 2, "name": "Jane", "age": 22, "city": "Los Angeles"}
        self.student3 = {"id": 3, "name": "Tom", "age": 23, "city": "Chicago"}

    def test_get_student_list(self):
        db.session.add_all([Student_schema.load(self.student1), Student_schema.load(self.student2), Student_schema.load(self.student3)])
        db.session.commit()
        response = self.client.get('/api/students')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 3)

    def test_get_student(self):
        db.session.add_all([Student_schema.load(self.student1), Student_schema.load(self.student2), Student_schema.load(self.student3)])
        db.session.commit()
        response = self.client.get('/api/students/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], "John")

    def test_get_student_invalid_id(self):
        db.session.add_all([Student_schema.load(self.student1), Student_schema.load(self.student2), Student_schema.load(self.student3)])
        db.session.commit()
        response = self.client.get('/api/students/0')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["message"], "Invalid ID: 0.")

    def test_get_student_not_found(self):
        db.session.add_all([Student_schema.load(self.student1), Student_schema.load(self.student2), Student_schema.load(self.student3)])
        db.session.commit()
        response = self.client.get('/api/students/4')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["message"], "Student with ID: 4 does not exist")

    def test_add_student(self):
        response = self.client.post('/api/students', json=self.student1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], "John")

    def test_add_student_duplicate_id(self):
        db.session.add(Student_schema.load(self.student1))
        db.session.commit()
        response = self.client.post('/api/students', json=self.student1)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["message"], "Student with ID: 1 already exists")

    def test_update_student(self):
        db.session.add(Student_schema.load(self.student1))
        db.session.commit()
        self.student1["name"] = "Jack"
        response = self.client.put('/api/students', json=self.student1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], "Jack")

    def test_update_student_not_found(self):
        response = self.client.put('/api/students', json=self.student1)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["message"], "Student with ID: 1 not found")

    def test_delete_student(self):
        db.session.add(Student_schema.load(self.student1))
        db.session.commit()
        response = self.client.delete('/api/students/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "Student with ID: 1 successfully deleted")

    def test_delete_student_not_found(self):
        response = self.client.delete('/api/students/1')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["message"], "Student with ID: 1 not found")