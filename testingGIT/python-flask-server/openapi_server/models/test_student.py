from student import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db, ma
from openapi_server.models.student import Student, StudentSchema

class TestStudent(unittest.TestCase):

    def test_student_model(self):
        student = Student(id=1, name='John Doe', address='123 Main St', email='john.doe@example.com', phone='555-555-5555')
        self.assertEqual(student.id, 1)
        self.assertEqual(student.name, 'John Doe')
        self.assertEqual(student.address, '123 Main St')
        self.assertEqual(student.email, 'john.doe@example.com')
        self.assertEqual(student.phone, '555-555-5555')

    def test_student_schema_dump(self):
        student = Student(id=1, name='John Doe', address='123 Main St', email='john.doe@example.com', phone='555-555-5555')
        student_schema = StudentSchema()
        result = student_schema.dump(student)
        expected_result = {"id": 1, "name": "John Doe", "address": "123 Main St", "email": "john.doe@example.com", "phone": "555-555-5555"}
        self.assertEqual(result, expected_result)

    def test_student_schema_load(self):
        student_data = {"id": 1, "name": "John Doe", "address": "123 Main St", "email": "john.doe@example.com", "phone": "555-555-5555"}
        student_schema = StudentSchema()
        result = student_schema.load(student_data)
        expected_result = Student(id=1, name='John Doe', address='123 Main St', email='john.doe@example.com', phone='555-555-5555')
        self.assertEqual(result, expected_result)

    def test_student_schema_load_multiple(self):
        students_data = [{"id": 1, "name": "John Doe", "address": "123 Main St", "email": "john.doe@example.com", "phone": "555-555-5555"}, {"id": 2, "name": "Jane Doe", "address": "456 Second St", "email": "jane.doe@example.com", "phone": "555-555-5556"}]
        student_schema = StudentSchema(many=True)
        result = student_schema.load(students_data)
        expected_result = [Student(id=1, name='John Doe', address='123 Main St', email='john.doe@example.com', phone='555-555-5555'), Student(id=2, name='Jane Doe', address='456 Second St', email='jane.doe@example.com', phone='555-555-5556')]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()