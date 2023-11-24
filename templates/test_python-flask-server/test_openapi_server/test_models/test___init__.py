from python-flask-server.openapi_server.models.__init__ import *
import unittest
from openapi_server.models.course import Course, Course_schema, Courses_schema
from openapi_server.models.student import Student, Student_schema, Students_schema
from openapi_server.models.user import User
from openapi_server.config_test import db, app

class TestModels(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.course = Course(course_name="Maths", course_code="MTH101")
        self.student = Student(student_name="John Doe", student_email="johndoe@example.com")

    def test_course_model(self):
        db.session.add(self.course)
        db.session.commit()
        course = Course.query.filter_by(course_name="Maths").first()
        self.assertEqual(course.course_name, "Maths")
        self.assertEqual(course.course_code, "MTH101")

    def test_student_model(self):
        db.session.add(self.student)
        db.session.commit()
        student = Student.query.filter_by(student_name="John Doe").first()
        self.assertEqual(student.student_name, "John Doe")
        self.assertEqual(student.student_email, "johndoe@example.com")

if __name__ == '__main__':
    unittest.main()