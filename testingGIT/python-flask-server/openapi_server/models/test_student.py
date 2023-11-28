from student import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db
from openapi_server.models import Student, StudentSchema

class TestStudentModel(unittest.TestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_student(self):
        """
        Test creating a new Student model
        """
        student = Student(name='John Doe', address='123 Main St', email='johndoe@example.com', phone='555-555-5555')
        db.session.add(student)
        db.session.commit()

        assert student.id is not None
        assert student.name == 'John Doe'
        assert student.address == '123 Main St'
        assert student.email == 'johndoe@example.com'
        assert student.phone == '555-555-5555'

    def test_get_student(self):
        """
        Test getting a Student model
        """
        student = Student(name='John Doe', address='123 Main St', email='johndoe@example.com', phone='555-555-5555')
        db.session.add(student)
        db.session.commit()

        fetched_student = Student.query.get(student.id)
        assert fetched_student is not None
        assert fetched_student.id == student.id
        assert fetched_student.name == 'John Doe'
        assert fetched_student.address == '123 Main St'
        assert fetched_student.email == 'johndoe@example.com'
        assert fetched_student.phone == '555-555-5555'

    def test_update_student(self):
        """
        Test updating a Student model
        """
        student = Student(name='John Doe', address='123 Main St', email='johndoe@example.com', phone='555-555-5555')
        db.session.add(student)
        db.session.commit()

        student.name = 'Jane Doe'
        db.session.commit()

        fetched_student = Student.query.get(student.id)
        assert fetched_student is not None
        assert fetched_student.name == 'Jane Doe'

    def test_delete_student(self):
        """
        Test deleting a Student model
        """
        student = Student(name='John Doe', address='123 Main St', email='johndoe@example.com', phone='555-555-5555')
        db.session.add(student)
        db.session.commit()

        db.session.delete(student)
        db.session.commit()

        assert Student.query.get(student.id) is None

if __name__ == '__main__':
    unittest.main()