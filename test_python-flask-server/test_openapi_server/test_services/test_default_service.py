from python-flask-server.openapi_server.services.default_service import *
import unittest
from unittest.mock import MagicMock
from openapi_server.services.default_service import DefaultService

class TestDefaultService(unittest.TestCase):

    def setUp(self):
        self.default_service = DefaultService()

    def test_get_default_list(self):
        # Test case where there are defaults in the database
        expected_result = [{'id': 1, 'name': 'Default 1'}, {'id': 2, 'name': 'Default 2'}]
        pagination_sorting_mock = MagicMock(return_value=expected_result)
        self.default_service.pagination_sorting = pagination_sorting_mock
        result = self.default_service.get_default_list()
        self.assertEqual(result, expected_result)

        # Test case where there are no defaults in the database
        pagination_sorting_mock = MagicMock(return_value=[])
        self.default_service.pagination_sorting = pagination_sorting_mock
        with self.assertRaises(Exception) as context:
            self.default_service.get_default_list()
        self.assertEqual(str(context.exception), "No default found")

    def test_get_default(self):
        # Test case where default exists in the database
        expected_result = {'id': 1, 'name': 'Default 1'}
        Default_mock = MagicMock()
        Default_mock.query.filter().one_or_none.return_value = expected_result
        result = self.default_service.get_default(1)
        self.assertEqual(result, expected_result)

        # Test case where default does not exist in the database
        Default_mock = MagicMock()
        Default_mock.query.filter().one_or_none.return_value = None
        with self.assertRaises(Exception) as context:
            self.default_service.get_default(-1)
        self.assertEqual(str(context.exception), "Default with ID: -1 does not exist")

    def test_add_default(self):
        # Test case where default does not already exist in the database
        expected_result = {'id': 1, 'name': 'Default 1'}
        Default_mock = MagicMock()
        Default_mock.query.filter().one_or_none.return_value = None
        Default_schema_mock = MagicMock(return_value=expected_result)
        self.default_service.Default_schema.load = Default_schema_mock
        self.default_service.db.session.add = MagicMock()
        self.default_service.db.session.commit = MagicMock()
        result = self.default_service.add_default(expected_result)
        self.assertEqual(result, expected_result)

        # Test case where default already exists in the database
        Default_mock = MagicMock()
        Default_mock.query.filter().one_or_none.return_value = expected_result
        with self.assertRaises(Exception) as context:
            self.default_service.add_default(expected_result)
        self.assertEqual(str(context.exception), "Default with ID: 1 already exists")

    def test_update_default(self):
        # Test case where default exists in the database
        expected_result = {'id': 1, 'name': 'Default 1'}
        Default_mock = MagicMock()
        Default_mock.query.filter().one_or_none.return_value = expected_result
        Default_schema_mock = MagicMock(return_value=expected_result)
        self.default_service.Default_schema.load = Default_schema_mock
        self.default_service.db.session.merge = MagicMock()
        self.default_service.db.session.commit = MagicMock()
        result = self.default_service.update_default(expected_result)
        self.assertEqual(result, expected_result)

        # Test case where default does not exist in the database
        Default_mock = MagicMock()
        Default_mock.query.filter().one_or_none.return_value = None
        with self.assertRaises(Exception) as context:
            self.default_service.update_default(expected_result)
        self.assertEqual(str(context.exception), "Default with ID: 1 not found")

    def test_delete_default(self):
        # Test case where default exists in the database
        expected_result = "Default with ID: 1 successfully deleted"
        Default_mock = MagicMock()
        Default_mock.query.filter().one_or_none.return_value = {'id': 1, 'name': 'Default 1'}
        self.default_service.db.session.delete = MagicMock()
        self.default_service.db.session.commit = MagicMock()
        result = self.default_service.delete_default(1)
        self.assertEqual(result, expected_result)

        # Test case where default does not exist in the database
        Default_mock = MagicMock()
        Default_mock.query.filter().one_or_none.return_value = None
        with self.assertRaises(Exception) as context:
            self.default_service.delete_default(-1)
        self.assertEqual(str(context.exception), "Default with ID: -1 not found")