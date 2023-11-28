from course import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db, ma
from openapi_server.models.course import Course, CourseSchema

class TestCourse(unittest.TestCase):
    def setUp(self):
        self.course1 = Course(id=1, name="Course 1", desc="Description 1")
        self.course2 = Course(id=2, name="Course 2", desc="Description 2")
        db.session.add(self.course1)
        db.session.add(self.course2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_course_schema(self):
        course_data = {
            'id': 1,
            'name': 'Course 1',
            'desc': 'Description 1'
        }
        course = Course_schema.load(course_data)
        self.assertEqual(course.id, 1)
        self.assertEqual(course.name, 'Course 1')
        self.assertEqual(course.desc, 'Description 1')
        serialized_course = Course_schema.dump(course)
        self.assertEqual(serialized_course, course_data)

    def test_get_all_courses(self):
        courses = Course.query.all()
        serialized_courses = Courses_schema.dump(courses)
        self.assertEqual(len(serialized_courses), 2)

    def test_get_course_by_id(self):
        course = Course.query.filter_by(id=1).first()
        serialized_course = Course_schema.dump(course)
        self.assertEqual(serialized_course['id'], 1)
        self.assertEqual(serialized_course['name'], 'Course 1')
        self.assertEqual(serialized_course['desc'], 'Description 1')

    def test_create_course(self):
        course_data = {
            'name': 'New Course',
            'desc': 'New Course Description'
        }
        course = Course_schema.load(course_data, session=db.session)
        db.session.add(course)
        db.session.commit()
        courses = Course.query.all()
        self.assertEqual(len(courses), 3)

    def test_update_course(self):
        course = Course.query.filter_by(id=1).first()
        course.name = 'Updated Course'
        db.session.commit()
        updated_course = Course.query.filter_by(id=1).first()
        self.assertEqual(updated_course.name, 'Updated Course')

    def test_delete_course(self):
        course = Course.query.filter_by(id=1).first()
        db.session.delete(course)
        db.session.commit()
        courses = Course.query.all()
        self.assertEqual(len(courses), 1)