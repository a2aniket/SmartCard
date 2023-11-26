from python-flask-server.openapi_server.services.course_service import *
import unittest
from openapi_server.services.pagination_sorting import pagination_sorting

class TestCourseService(unittest.TestCase):

    def test_get_course_list(self):
        """
        Test the get_course_list function to ensure it returns a list of courses in JSON format with a HTTP status code of 200.
        """
        response = CourseService.get_course_list()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_course(self):
        """
        Test the get_course function to ensure it retrieves a course by ID from the database.
        """
        existing_course = Course.query.first()
        response = CourseService.get_course(existing_course.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("id"), existing_course.id)

    def test_get_course_with_invalid_id(self):
        """
        Test the get_course function to ensure it raises a 404 error when an invalid ID is provided.
        """
        response = CourseService.get_course(-1)
        self.assertEqual(response.status_code, 404)

    def test_add_course(self):
        """
        Test the add_course function to ensure it adds a new course to the database.
        """
        course = {"id": 100, "name": "Test Course", "description": "This is a test course."}
        response = CourseService.add_course(course)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("id"), course.get("id"))

    def test_add_course_with_existing_id(self):
        """
        Test the add_course function to ensure it raises a 400 error when a course with the same id already exists.
        """
        existing_course = Course.query.first()
        course = {"id": existing_course.id, "name": "Test Course", "description": "This is a test course."}
        response = CourseService.add_course(course)
        self.assertEqual(response.status_code, 400)

    def test_update_course(self):
        """
        Test the update_course function to ensure it updates an existing course in the database.
        """
        existing_course = Course.query.first()
        updated_course = {"id": existing_course.id, "name": "Updated Test Course", "description": "This is an updated test course."}
        response = CourseService.update_course(updated_course)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("name"), updated_course.get("name"))

    def test_update_course_with_non_existing_id(self):
        """
        Test the update_course function to ensure it raises a 404 error when the course is not found.
        """
        non_existing_id = Course.query.order_by(Course.id.desc()).first().id + 1
        updated_course = {"id": non_existing_id, "name": "Updated Test Course", "description": "This is an updated test course."}
        response = CourseService.update_course(updated_course)
        self.assertEqual(response.status_code, 404)

    def test_delete_course(self):
        """
        Test the delete_course function to ensure it deletes the course with the specified id.
        """
        existing_course = Course.query.first()
        response = CourseService.delete_course(existing_course.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), f"Course with ID: {existing_course.id} successfully deleted")

    def test_delete_course_with_non_existing_id(self):
        """
        Test the delete_course function to ensure it raises a 400 error when the course is not found.
        """
        non_existing_id = Course.query.order_by(Course.id.desc()).first().id + 1
        response = CourseService.delete_course(non_existing_id)
        self.assertEqual(response.status_code, 400)