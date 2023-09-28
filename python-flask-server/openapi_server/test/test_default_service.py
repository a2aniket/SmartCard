import unittest
from unittest.mock import patch
from openapi_server.services.default_service import DefaultService

class TestDefaultService(unittest.TestCase):

    def setUp(self):
        self.default_service = DefaultService()

    def test_get_default_list(self):
        """
        Test for getting list of all defaults from the database
        """
        with patch('openapi_server.services.default_service.Default.query') as mock_query:
            mock_query.return_value.all.return_value = [{'id': 1, 'name': 'default1'}, {'id': 2, 'name': 'default2'}]
            response = self.default_service.get_default_list()
            self.assertEqual(len(response), 2)
            self.assertEqual(response[0]['id'], 1)
            self.assertEqual(response[0]['name'], 'default1')
            self.assertEqual(response[1]['id'], 2)
            self.assertEqual(response[1]['name'], 'default2')

    def test_get_default(self):
        """
        Test for getting a default by ID from the database
        """
        with patch('openapi_server.services.default_service.Default.query') as mock_query:
            mock_query.return_value.filter.return_value.one_or_none.return_value = {'id': 1, 'name': 'default1'}
            response = self.default_service.get_default(1)
            self.assertEqual(response['id'], 1)
            self.assertEqual(response['name'], 'default1')

    def test_get_default_with_invalid_id(self):
        """
        Test for getting a default by invalid ID from the database
        """
        with self.assertRaisesRegex(Exception, "Invalid ID: -1."):
            self.default_service.get_default(-1)

    def test_get_default_not_found(self):
        """
        Test for getting a default which does not exist in the database
        """
        with patch('openapi_server.services.default_service.Default.query') as mock_query:
            mock_query.return_value.filter.return_value.one_or_none.return_value = None
            with self.assertRaisesRegex(Exception, "Default with ID: 1 does not exist"):
                self.default_service.get_default(1)

    def test_add_default(self):
        """
        Test for adding a new default to the database
        """
        default = {'id': 1, 'name': 'default1'}
        with patch('openapi_server.services.default_service.Default.query') as mock_query:
            mock_query.return_value.filter.return_value.one_or_none.return_value = None
            with patch('openapi_server.services.default_service.db.session') as mock_session:
                mock_session.commit.return_value = None
                response = self.default_service.add_default(default)
                self.assertEqual(response['id'], 1)
                self.assertEqual(response['name'], 'default1')

    def test_add_default_already_exists(self):
        """
        Test for adding a new default which already exists in the database
        """
        default = {'id': 1, 'name': 'default1'}
        with patch('openapi_server.services.default_service.Default.query') as mock_query:
            mock_query.return_value.filter.return_value.one_or_none.return_value = default
            with self.assertRaisesRegex(Exception, "Default with ID: 1 already exists"):
                self.default_service.add_default(default)

    def test_update_default(self):
        """
        Test for updating an existing default in the database
        """
        default = {'id': 1, 'name': 'default_updated'}
        existing_default = {'id': 1, 'name': 'default1'}
        with patch('openapi_server.services.default_service.Default.query') as mock_query:
            mock_query.return_value.filter.return_value.one_or_none.return_value = existing_default
            with patch('openapi_server.services.default_service.db.session') as mock_session:
                mock_session.commit.return_value = None
                response = self.default_service.update_default(default)
                self.assertEqual(response['id'], 1)
                self.assertEqual(response['name'], 'default_updated')

    def test_update_default_not_found(self):
        """
        Test for updating a default which does not exist in the database
        """
        default = {'id': 1, 'name': 'default1'}
        with patch('openapi_server.services.default_service.Default.query') as mock_query:
            mock_query.return_value.filter.return_value.one_or_none.return_value = None
            with self.assertRaisesRegex(Exception, "Default with ID: 1 not found"):
                self.default_service.update_default(default)

    def test_delete_default(self):
        """
        Test for deleting a default from the database
        """
        with patch('openapi_server.services.default_service.Default.query') as mock_query:
            mock_query.return_value.filter.return_value.one_or_none.return_value = {'id': 1, 'name': 'default1'}
            with patch('openapi_server.services.default_service.db.session') as mock_session:
                mock_session.commit.return_value = None
                response = self.default_service.delete_default(1)
                self.assertEqual(response, "Default with ID: 1 successfully deleted")

    def test_delete_default_not_found(self):
        """
        Test for deleting a default which does not exist in the database
        """
        with patch('openapi_server.services.default_service.Default.query') as mock_query:
            mock_query.return_value.filter.return_value.one_or_none.return_value = None
            with self.assertRaisesRegex(Exception, "Default with ID: 1 not found"):
                self.default_service.delete_default(1)

if __name__ == '__main__':
    unittest.main()