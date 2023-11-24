from python-flask-server.openapi_server.services.student_service import *
import unittest
from openapi_server.models.student import Student, Student_schema, Students_schema
from openapi_server.services.pagination_sorting import pagination_sorting
from openapi_server.services.student_service import StudentService

class TestStudentService(unittest.TestCase):

    def setUp(self):
        self.student1 = {"id": 1, "name": "John Doe", "age": 20}
        self.student2 = {"id": 2, "name": "Jane Smith", "age": 22}
        self.student3 = {"id": 3, "name": "Bob Johnson", "age": 25}

        with app.app_context():
            db.create_all()
            new_student1 = Student_schema.load(self.student1, session=db.session)
            new_student2 = Student_schema.load(self.student2, session=db.session)
            db.session.add(new_student1)
            db.session.add(new_student2)
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_student_list(self):
        students = StudentService.get_student_list()
        self.assertEqual(len(students), 2)
        self.assertEqual(students[0]["id"], self.student1["id"])
        self.assertEqual(students[1]["id"], self.student2["id"])
        
    def test_get_student(self):
        student = StudentService.get_student(self.student1["id"])
        self.assertEqual(student["id"], self.student1["id"])
        self.assertEqual(student["name"], self.student1["name"])
        self.assertEqual(student["age"], self.student1["age"])
        
    def test_get_student_not_found(self):
        with self.assertRaises(Exception) as context:
            StudentService.get_student(4)
        self.assertTrue("Student with ID: 4 does not exist" in str(context.exception))
        
    def test_add_student(self):
        student3 = {"id": 3, "name": "Bob Johnson", "age": 25}
        new_student = StudentService.add_student(student3)
        self.assertEqual(new_student["id"], student3["id"])
        self.assertEqual(new_student["name"], student3["name"])
        self.assertEqual(new_student["age"], student3["age"])
        
    def test_add_existing_student(self):
        with self.assertRaises(Exception) as context:
            StudentService.add_student(self.student1)
        self.assertTrue("Student with ID: 1 already exists" in str(context.exception))
        
    def test_update_student(self):
        updated_student = {"id": self.student1["id"], "name": "John Smith", "age": 21}
        updated_student = StudentService.update_student(updated_student)
        self.assertEqual(updated_student["id"], self.student1["id"])
        self.assertEqual(updated_student["name"], "John Smith")
        self.assertEqual(updated_student["age"], 21)
        
    def test_update_student_not_found(self):
        student4 = {"id": 4, "name": "Tom Johnson", "age": 23}
        with self.assertRaises(Exception) as context:
            StudentService.update_student(student4)
        self.assertTrue("Student with ID: 4 not found" in str(context.exception))
        
    def test_delete_student(self):
        message = StudentService.delete_student(self.student1["id"])
        self.assertEqual(message, f"Student with ID: {self.student1['id']} successfully deleted")
        
    def test_delete_student_not_found(self):
        with self.assertRaises(Exception) as context:
            StudentService.delete_student(4)
        self.assertTrue("Student with ID: 4 not found" in str(context.exception))