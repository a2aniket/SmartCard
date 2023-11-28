from services.student_service import *
Here is a comprehensive set of unit tests for the given code snippet:

```
import unittest
from unittest.mock import patch, MagicMock
from openapi_server.services.pagination_sorting import pagination_sorting
from openapi_server.models.student import Student, Student_schema, Students_schema
from openapi_server.services.student_service import StudentService

class TestStudentService(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.student_service = StudentService()

    def test_get_student_list_with_no_students(self):
        with patch('openapi_server.services.student_service.pagination_sorting', return_value=[]):
            with self.assertRaisesRegex(Exception, 'No student found'):
                self.student_service.get_student_list()

    def test_get_student_list_with_students(self):
        with patch('openapi_server.services.student_service.pagination_sorting', return_value=[Student(id=1, name='John Doe', age=20)]):
            result = self.student_service.get_student_list()
            self.assertEqual(result, Students_schema.dump([Student(id=1, name='John Doe', age=20)], many=True))

    def test_get_student_with_invalid_id(self):
        with self.assertRaisesRegex(Exception, 'Invalid ID: -1.'):
            self.student_service.get_student(-1)

    def test_get_student_with_non_existent_id(self):
        with patch.object(Student, 'query') as mock_query:
            mock_query.filter.return_value.one_or_none.return_value = None
            with self.assertRaisesRegex(Exception, 'Student with ID: 1 does not exist'):
                self.student_service.get_student(1)

    def test_get_student_with_valid_id(self):
        with patch.object(Student, 'query') as mock_query:
            mock_query.filter.return_value.one_or_none.return_value = Student(id=1, name='John Doe', age=20)
            result = self.student_service.get_student(1)
            self.assertEqual(result, Student_schema.dump(Student(id=1, name='John Doe', age=20)))

    def test_add_student_with_existing_id(self):
        with patch.object(Student, 'query') as mock_query:
            mock_query.filter.return_value.one_or_none.return_value = Student(id=1, name='John Doe', age=20)
            with self.assertRaisesRegex(Exception, 'Student with ID: 1 already exists'):
                self.student_service.add_student({'id': 1, 'name': 'Jane Doe', 'age': 21})

    def test_add_student_with_new_id(self):
        with patch.object(Student, 'query') as mock_query:
            mock_query.filter.return_value.one_or_none.return_value = None
            with patch.object(Student_schema, 'load') as mock_load:
                mock_student = MagicMock()
                mock_student.id = 2
                mock_load.return_value = mock_student
                with patch.object(Student, 'query') as mock_query:
                    with patch.object(db.session, 'add') as mock_add:
                        with patch.object(db.session, 'commit') as mock_commit:
                            result = self.student_service.add_student({'id': 2, 'name': 'Jane Doe', 'age': 21})
                            self.assertEqual(result, Student_schema.dump(mock_student))
                            mock_add.assert_called_once_with(mock_student)
                            mock_commit.assert_called_once()

    def test_update_student_with_non_existent_id(self):
        with patch.object(Student, 'query') as mock_query:
            mock_query.filter.return_value.one_or_none.return_value = None
            with self.assertRaisesRegex(Exception, 'Student with ID: 1 not found'):
                self.student_service.update_student({'id': 1, 'name': 'Jane Doe', 'age': 21})

    def test_update_student_with_existent_id(self):
        with patch.object(Student, 'query') as mock_query:
            mock_query.filter.return_value.one_or_none.return_value = Student(id=1, name='John Doe', age=20)
            with patch.object(Student_schema, 'load') as mock_load:
                mock_student = MagicMock()
                mock_student.id = 1
                mock_load.return_value = mock_student
                with patch.object(Student, 'query') as mock_query:
                    with patch.object(db.session, 'merge') as mock_merge:
                        with patch.object(db.session, 'commit') as mock_commit:
                            result = self.student_service.update_student({'id': 1, 'name': 'Jane Doe', 'age': 21})
                            self.assertEqual(result, Student_schema.dump(mock_student))
                            mock_merge.assert_called_once_with(mock_student)
                            mock_commit.assert_called_once()

    def test_delete_student_with_non_existent_id(self):
        with patch.object(Student, 'query') as mock_query:
            mock_query.filter.return_value.one_or_none.return_value = None
            with self.assertRaisesRegex(Exception, 'Student with ID: 1 not found'):
                self.student_service.delete_student(1)

    def test_delete_student_with_existent_id(self):
        with patch.object(Student, 'query') as mock_query:
            mock_query.filter.return_value.one_or_none.return_value = Student(id=1, name='John Doe', age=20)
            with patch.object(Student, 'query') as mock_query:
                with patch.object(db.session, 'delete') as mock_delete:
                    with patch.object(db.session, 'commit') as mock_commit:
                        result = self.student_service.delete_student(1)
                        self.assertEqual(result, 'Student with ID: 1 successfully deleted')
                        mock_delete.assert_called_once_with(Student(id=1, name='John Doe', age=20))
                        mock_commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()