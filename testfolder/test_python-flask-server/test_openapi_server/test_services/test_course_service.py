from python-flask-server.openapi_server.services.course_service import *
import unittest
from unittest.mock import patch
from openapi_server.config_test import db
from openapi_server.models.course import Course, Course_schema, Courses_schema
from openapi_server.services.pagination_sorting import pagination_sorting
from openapi_server.services.course_service import CourseService

class TestCourseService(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_course_list(self):
        """
        Test getting a list of all courses
        """
        course1 = Course(name="Course 1", description="Description 1", credit_hours=3)
        course2 = Course(name="Course 2", description="Description 2", credit_hours=4)
        db.session.add(course1)
        db.session.add(course2)
        db.session.commit()

        courses = CourseService.get_course_list()
        self.assertEqual(len(courses), 2)
        self.assertEqual(courses[0]["name"], course1.name)
        self.assertEqual(courses[1]["name"], course2.name)

    def test_get_course(self):
        """
        Test getting a course by ID
        """
        course = Course(name="Course 1", description="Description 1", credit_hours=3)
        db.session.add(course)
        db.session.commit()

        retrieved_course = CourseService.get_course(course.id)
        self.assertEqual(retrieved_course["name"], course.name)

    def test_get_course_with_invalid_id(self):
        """
        Test getting a course with an invalid ID
        """
        with self.assertRaises(Exception):
            CourseService.get_course(-1)

    def test_get_course_with_nonexistent_id(self):
        """
        Test getting a course with a nonexistent ID
        """
        with self.assertRaises(Exception):
            CourseService.get_course(999)

    def test_add_course(self):
        """
        Test adding a new course
        """
        course = {"name": "New Course", "description": "New Description", "credit_hours": 3, "id": 1}

        new_course = CourseService.add_course(course)
        self.assertEqual(new_course["name"], course["name"])

    def test_add_course_with_existing_id(self):
        """
        Test adding a new course with an existing ID
        """
        course1 = Course(name="Course 1", description="Description 1", credit_hours=3, id=1)
        db.session.add(course1)
        db.session.commit()

        course2 = {"name": "Course 2", "description": "Description 2", "credit_hours": 4, "id": 1}

        with self.assertRaises(Exception):
            CourseService.add_course(course2)

    def test_update_course(self):
        """
        Test updating an existing course
        """
        course = Course(name="Course 1", description="Description 1", credit_hours=3)
        db.session.add(course)
        db.session.commit()

        updated_course = {"name": "Updated Course", "description": "Updated Description", "credit_hours": 4, "id": course.id}

        CourseService.update_course(updated_course)

        retrieved_course = CourseService.get_course(course.id)
        self.assertEqual(retrieved_course["name"], updated_course["name"])

    def test_update_course_with_nonexistent_id(self):
        """
        Test updating a course with a nonexistent ID
        """
        course = {"name": "New Course", "description": "New Description", "credit_hours": 3, "id": 999}

        with self.assertRaises(Exception):
            CourseService.update_course(course)

    def test_delete_course(self):
        """
        Test deleting a course
        """
        course = Course(name="Course 1", description="Description 1", credit_hours=3)
        db.session.add(course)
        db.session.commit()

        CourseService.delete_course(course.id)

        with self.assertRaises(Exception):
            CourseService.get_course(course.id)

    def test_delete_course_with_nonexistent_id(self):
        """
        Test deleting a course with a nonexistent ID
        """
        with self.assertRaises(Exception):
            CourseService.delete_course(999)

if __name__ == '__main__':
    unittest.main()