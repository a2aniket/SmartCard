from course import *
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
        course = Course(name='test', desc='test description')
        db.session.add(course)
        db.session.commit()

        self.assertEqual(course.id, 1)
        self.assertEqual(course.name, 'test')
        self.assertEqual(course.desc, 'test description')

    def test_course_schema(self):
        course = Course(name='test', desc='test description')
        db.session.add(course)
        db.session.commit()

        serialized_course = Course_schema.dump(course)
        self.assertEqual(serialized_course['id'], 1)
        self.assertEqual(serialized_course['name'], 'test')
        self.assertEqual(serialized_course['desc'], 'test description')
        
    def test_courses_schema(self):
        course1 = Course(name='test1', desc='test description 1')
        course2 = Course(name='test2', desc='test description 2')
        
        db.session.add_all([course1, course2])
        db.session.commit()
        
        serialized_courses = Courses_schema.dump([course1, course2])
        self.assertEqual(len(serialized_courses), 2)
        self.assertEqual(serialized_courses[0]['id'], 1)
        self.assertEqual(serialized_courses[0]['name'], 'test1')
        self.assertEqual(serialized_courses[0]['desc'], 'test description 1')
        self.assertEqual(serialized_courses[1]['id'], 2)
        self.assertEqual(serialized_courses[1]['name'], 'test2')
        self.assertEqual(serialized_courses[1]['desc'], 'test description 2')