from python-flask-server.openapi_server.models.course import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db, ma
from openapi_server.models.course import Course, CourseSchema

class TestCourse(unittest.TestCase):
    def setUp(self):
        self.course1 = Course(id=1, name="Course 1", desc="Course 1 description")
        self.course2 = Course(id=2, name="Course 2", desc="Course 2 description")
        db.session.add(self.course1)
        db.session.add(self.course2)
        db.session.commit()

    def test_course_schema(self):
        course_data = {'id': 1, 'name': 'Course 1', 'desc': 'Course 1 description'}
        result = Course_schema.load(course_data)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.name, 'Course 1')
        self.assertEqual(result.desc, 'Course 1 description')

    def test_get_all_courses(self):
        result = Course.query.all()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].name, 'Course 1')
        self.assertEqual(result[0].desc, 'Course 1 description')
        self.assertEqual(result[1].id, 2)
        self.assertEqual(result[1].name, 'Course 2')
        self.assertEqual(result[1].desc, 'Course 2 description')

    def test_get_course_by_id(self):
        result = Course.query.filter_by(id=1).first()
        self.assertEqual(result.id, 1)
        self.assertEqual(result.name, 'Course 1')
        self.assertEqual(result.desc, 'Course 1 description')

    def test_create_course(self):
        course_data = {'name': 'Course 3', 'desc': 'Course 3 description'}
        result = Course_schema.load(course_data)
        db.session.add(result)
        db.session.commit()
        self.assertEqual(result.id, 3)
        self.assertEqual(result.name, 'Course 3')
        self.assertEqual(result.desc, 'Course 3 description')

    def test_update_course(self):
        course_data = {'name': 'Updated Course', 'desc': 'Updated Course description'}
        result = Course.query.filter_by(id=1).first()
        result.name = course_data['name']
        result.desc = course_data['desc']
        db.session.commit()
        updated_result = Course.query.filter_by(id=1).first()
        self.assertEqual(updated_result.id, 1)
        self.assertEqual(updated_result.name, 'Updated Course')
        self.assertEqual(updated_result.desc, 'Updated Course description')

    def test_delete_course(self):
        result = Course.query.filter_by(id=1).first()
        db.session.delete(result)
        db.session.commit()
        deleted_result = Course.query.filter_by(id=1).first()
        self.assertIsNone(deleted_result)

if __name__ == '__main__':
    unittest.main()