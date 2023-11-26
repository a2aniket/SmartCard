from python-flask-server.openapi_server.services.student_service import *
import unittest
from unittest.mock import MagicMock
from openapi_server.services.pagination_sorting import pagination_sorting
from openapi_server.models.student import Student, Student_schema, Students_schema
from openapi_server.config_test import db
from openapi_server.student_service import StudentService


class TestStudentService(unittest.TestCase):

    def setUp(self):
        db.drop_all()
        db.create_all()

    def test_get_student_list(self):
        # Test case when no students are present
        self.assertEqual(StudentService.get_student_list(), [])
        # Test case when students are present
        student = Student(id=1, name="John", age=20)
        db.session.add(student)
        db.session.commit()
        expected_output = [{"id": 1, "name": "John", "age": 20}]
        self.assertEqual(StudentService.get_student_list(), expected_output)

    def test_get_student(self):
        # Test case when student is present
        student = Student(id=1, name="John", age=20)
        db.session.add(student)
        db.session.commit()
        expected_output = {"id": 1, "name": "John", "age": 20}
        self.assertEqual(StudentService.get_student(1), expected_output)
        # Test case when student with given id not present
        with self.assertRaises(Exception):
            StudentService.get_student(2)
        # Test case when id is less than 1
        with self.assertRaises(Exception):
            StudentService.get_student(-1)

    def test_add_student(self):
        # Test case when student with given id is not present
        student = {"id": 1, "name": "John", "age": 20}
        expected_output = {"id": 1, "name": "John", "age": 20}
        self.assertEqual(StudentService.add_student(student), expected_output)
        # Test case when student with given id is already present
        with self.assertRaises(Exception):
            StudentService.add_student(student)
        
    def test_update_student(self):
        # Test case when student is present
        student = Student(id=1, name="John", age=20)
        db.session.add(student)
        db.session.commit()
        update_student = {"id": 1, "name": "John Doe", "age": 21}
        expected_output = {"id": 1, "name": "John Doe", "age": 21}
        self.assertEqual(StudentService.update_student(update_student), expected_output)
        # Test case when student with given id not present
        with self.assertRaises(Exception):
            StudentService.update_student(update_student)

    def test_delete_student(self):
        # Test case when student is present
        student = Student(id=1, name="John", age=20)
        db.session.add(student)
        db.session.commit()
        expected_output = "Student with ID: 1 successfully deleted"
        self.assertEqual(StudentService.delete_student(1), expected_output)
        # Test case when student with given id not present
        with self.assertRaises(Exception):
            StudentService.delete_student(2)

if __name__ == '__main__':
    unittest.main()