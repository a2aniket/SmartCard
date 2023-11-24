from python-flask-server.openapi_server.models.course import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db, ma
from openapi_server.models.course import Course, CourseSchema

class TestCourse(unittest.TestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_course_model(self):
        course = Course(name='Test', desc='Test Description')
        db.session.add(course)
        db.session.commit()

        queried_course = Course.query.filter_by(name='Test').first()
        self.assertEqual(queried_course.name, 'Test')
        self.assertEqual(queried_course.desc, 'Test Description')

    def test_course_schema(self):
        course = Course(name='Test', desc='Test Description')
        serialized_course = Course_schema.dump(course)
        self.assertEqual(serialized_course['name'], 'Test')
        self.assertEqual(serialized_course['desc'], 'Test Description')

    def test_courses_schema(self):
        course1 = Course(name='Test1', desc='Test 1 Description')
        course2 = Course(name='Test2', desc='Test 2 Description')
        db.session.add_all([course1, course2])
        db.session.commit()

        serialized_courses = Courses_schema.dump(Course.query.all())
        self.assertEqual(len(serialized_courses), 2)
        self.assertEqual(serialized_courses[0]['name'], 'Test1')
        self.assertEqual(serialized_courses[0]['desc'], 'Test 1 Description')
        self.assertEqual(serialized_courses[1]['name'], 'Test2')
        self.assertEqual(serialized_courses[1]['desc'], 'Test 2 Description')