from python-flask-server.openapi_server.models.student import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db, ma
from openapi_server.models.student import Student, StudentSchema

class TestStudentModel(unittest.TestCase):
    
    def test_student_model_creation(self):
        test_student = Student(id=1, name='John Doe', address='123 Main St', email='johndoe@example.com', phone='555-555-5555')
        self.assertEqual(test_student.id, 1)
        self.assertEqual(test_student.name, 'John Doe')
        self.assertEqual(test_student.address, '123 Main St')
        self.assertEqual(test_student.email, 'johndoe@example.com')
        self.assertEqual(test_student.phone, '555-555-5555')
        
    def test_student_schema_dump(self):
        test_student = Student(id=1, name='John Doe', address='123 Main St', email='johndoe@example.com', phone='555-555-5555')
        student_schema = StudentSchema()
        dump_result = student_schema.dump(test_student)
        self.assertEqual(dump_result['id'], 1)
        self.assertEqual(dump_result['name'], 'John Doe')
        self.assertEqual(dump_result['address'], '123 Main St')
        self.assertEqual(dump_result['email'], 'johndoe@example.com')
        self.assertEqual(dump_result['phone'], '555-555-5555')

    def test_student_schema_load(self):
        test_student_data = {'id': 1, 'name': 'John Doe', 'address': '123 Main St', 'email': 'johndoe@example.com', 'phone': '555-555-5555'}
        student_schema = StudentSchema()
        load_result = student_schema.load(test_student_data)
        self.assertEqual(load_result.id, 1)
        self.assertEqual(load_result.name, 'John Doe')
        self.assertEqual(load_result.address, '123 Main St')
        self.assertEqual(load_result.email, 'johndoe@example.com')
        self.assertEqual(load_result.phone, '555-555-5555')

    def test_students_schema_dump(self):
        test_students = [Student(id=1, name='John Doe', address='123 Main St', email='johndoe@example.com', phone='555-555-5555'),
                         Student(id=2, name='Jane Smith', address='456 Elm St', email='janesmith@example.com', phone='555-555-5555')]
        students_schema = StudentSchema(many=True)
        dump_result = students_schema.dump(test_students)
        self.assertEqual(len(dump_result), 2)
        self.assertEqual(dump_result[0]['id'], 1)
        self.assertEqual(dump_result[0]['name'], 'John Doe')
        self.assertEqual(dump_result[0]['address'], '123 Main St')
        self.assertEqual(dump_result[0]['email'], 'johndoe@example.com')
        self.assertEqual(dump_result[0]['phone'], '555-555-5555')
        self.assertEqual(dump_result[1]['id'], 2)
        self.assertEqual(dump_result[1]['name'], 'Jane Smith')
        self.assertEqual(dump_result[1]['address'], '456 Elm St')
        self.assertEqual(dump_result[1]['email'], 'janesmith@example.com')
        self.assertEqual(dump_result[1]['phone'], '555-555-5555')

    def test_students_schema_load(self):
        test_students_data = [{'id': 1, 'name': 'John Doe', 'address': '123 Main St', 'email': 'johndoe@example.com', 'phone': '555-555-5555'},
                              {'id': 2, 'name': 'Jane Smith', 'address': '456 Elm St', 'email': 'janesmith@example.com', 'phone': '555-555-5555'}]
        students_schema = StudentSchema(many=True)
        load_result = students_schema.load(test_students_data)
        self.assertEqual(len(load_result), 2)
        self.assertEqual(load_result[0].id, 1)
        self.assertEqual(load_result[0].name, 'John Doe')
        self.assertEqual(load_result[0].address, '123 Main St')
        self.assertEqual(load_result[0].email, 'johndoe@example.com')
        self.assertEqual(load_result[0].phone, '555-555-5555')
        self.assertEqual(load_result[1].id, 2)
        self.assertEqual(load_result[1].name, 'Jane Smith')
        self.assertEqual(load_result[1].address, '456 Elm St')
        self.assertEqual(load_result[1].email, 'janesmith@example.com')
        self.assertEqual(load_result[1].phone, '555-555-5555')