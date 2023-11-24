from python-flask-server.openapi_server.models.student import *
import unittest

from openapi_server import db, Student, Student_schema, Students_schema


class TestStudentModel(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_student(self):
        """Test creating a student"""
        student_data = {
            'name': 'John Doe',
            'address': '123 Main St',
            'email': 'johndoe@example.com',
            'phone': '555-555-5555'
        }
        student = Student(**student_data)
        db.session.add(student)
        db.session.commit()
        self.assertEqual(student.id, 1)

    def test_get_all_students(self):
        """Test getting all students"""
        student_data_1 = {
            'name': 'John Doe',
            'address': '123 Main St',
            'email': 'johndoe@example.com',
            'phone': '555-555-5555'
        }
        student_data_2 = {
            'name': 'Jane Doe',
            'address': '456 Main St',
            'email': 'janedoe@example.com',
            'phone': '555-555-5555'
        }
        student_1 = Student(**student_data_1)
        student_2 = Student(**student_data_2)
        db.session.add_all([student_1, student_2])
        db.session.commit()
        students = Student.query.all()
        self.assertEqual(len(students), 2)

    def test_get_student_by_id(self):
        """Test getting a student by id"""
        student_data = {
            'name': 'John Doe',
            'address': '123 Main St',
            'email': 'johndoe@example.com',
            'phone': '555-555-5555'
        }
        student = Student(**student_data)
        db.session.add(student)
        db.session.commit()
        student = Student.query.filter_by(id=1).first()
        self.assertIsNotNone(student)

    def test_update_student(self):
        """Test updating a student"""
        student_data = {
            'name': 'John Doe',
            'address': '123 Main St',
            'email': 'johndoe@example.com',
            'phone': '555-555-5555'
        }
        updated_student_data = {
            'name': 'Jane Doe',
            'address': '456 Main St',
            'email': 'janedoe@example.com',
            'phone': '555-555-5555'
        }
        student = Student(**student_data)
        db.session.add(student)
        db.session.commit()
        student.name = updated_student_data['name']
        student.address = updated_student_data['address']
        student.email = updated_student_data['email']
        student.phone = updated_student_data['phone']
        db.session.commit()
        updated_student = Student.query.filter_by(id=1).first()
        self.assertEqual(updated_student.name, updated_student_data['name'])
        self.assertEqual(updated_student.address, updated_student_data['address'])
        self.assertEqual(updated_student.email, updated_student_data['email'])
        self.assertEqual(updated_student.phone, updated_student_data['phone'])

    def test_delete_student(self):
        """Test deleting a student"""
        student_data = {
            'name': 'John Doe',
            'address': '123 Main St',
            'email': 'johndoe@example.com',
            'phone': '555-555-5555'
        }
        student = Student(**student_data)
        db.session.add(student)
        db.session.commit()
        student = Student.query.filter_by(id=1).first()
        db.session.delete(student)
        db.session.commit()
        deleted_student = Student.query.filter_by(id=1).first()
        self.assertIsNone(deleted_student)