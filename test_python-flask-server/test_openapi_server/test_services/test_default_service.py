from python-flask-server.openapi_server.services.default_service import *
import unittest
from unittest.mock import patch
from openapi_server.services.pagination_sorting import pagination_sorting
from openapi_server.models.default import Default, Default_schema

class TestDefaultService(unittest.TestCase):

    @patch('openapi_server.config_test.db.session.query')
    def test_get_default_list(self, mock_query):
        mock_query.return_value.all.return_value = [
            Default(id=1, name="default1"),
            Default(id=2, name="default2")
        ]
        expected_result = [
            Default_schema.dump(Default(id=1, name="default1")),
            Default_schema.dump(Default(id=2, name="default2"))
        ]
        result = DefaultService.get_default_list()
        self.assertEqual(result, expected_result)
        mock_query.assert_called_once_with(Default)

    @patch('openapi_server.config_test.db.session.query')
    def test_get_default_list_no_defaults(self, mock_query):
        mock_query.return_value.all.return_value = []
        with self.assertRaisesRegex(Exception, "No default found"):
            result = DefaultService.get_default_list()

    @patch('openapi_server.config_test.db.session.query')
    def test_get_default(self, mock_query):
        mock_query.return_value.filter.return_value.one_or_none.return_value = Default(id=1, name="default")
        expected_result = Default_schema.dump(Default(id=1, name="default"))
        result = DefaultService.get_default(1)
        self.assertEqual(result, expected_result)
        mock_query.assert_called_once_with(Default)
        mock_query.return_value.filter.assert_called_once_with(Default.id == 1)
        mock_query.return_value.filter.return_value.one_or_none.assert_called_once()

    @patch('openapi_server.config_test.db.session.query')
    def test_get_default_not_found(self, mock_query):
        mock_query.return_value.filter.return_value.one_or_none.return_value = None
        with self.assertRaisesRegex(Exception, "Default with ID: 0 does not exist"):
            result = DefaultService.get_default(0)

    @patch('openapi_server.config_test.db.session.add')
    @patch('openapi_server.config_test.db.session.commit')
    @patch('openapi_server.config_test.db.session.query')
    def test_add_default(self, mock_query, mock_commit, mock_add):
        mock_query.return_value.filter.return_value.one_or_none.return_value = None
        mock_commit.return_value = None
        input_default = Default(id=1, name="default")
        input_dict = Default_schema.dump(input_default)
        expected_result = Default_schema.dump(Default(id=1, name="default"))
        result = DefaultService.add_default(input_dict)
        self.assertEqual(result, expected_result)
        mock_query.assert_called_once_with(Default)
        mock_query.return_value.filter.assert_called_once_with(Default.id == 1)
        mock_query.return_value.filter.return_value.one_or_none.assert_called_once()
        mock_add.assert_called_once_with(input_default)
        mock_commit.assert_called_once()

    @patch('openapi_server.config_test.db.session.query')
    def test_add_default_already_exists(self, mock_query):
        mock_query.return_value.filter.return_value.one_or_none.return_value = Default(id=1, name="default")
        with self.assertRaisesRegex(Exception, "Default with ID: 1 already exists"):
            result = DefaultService.add_default(Default_schema.dump(Default(id=1, name="default")))

    @patch('openapi_server.config_test.db.session.merge')
    @patch('openapi_server.config_test.db.session.commit')
    @patch('openapi_server.config_test.db.session.query')
    def test_update_default(self, mock_query, mock_commit, mock_merge):
        mock_query.return_value.filter.return_value.one_or_none.return_value = Default(id=1, name="default")
        mock_commit.return_value = None
        input_default = Default(id=1, name="new_default")
        input_dict = Default_schema.dump(input_default)
        expected_result = Default_schema.dump(Default(id=1, name="new_default"))
        result = DefaultService.update_default(input_dict)
        self.assertEqual(result, expected_result)
        mock_query.assert_called_once_with(Default)
        mock_query.return_value.filter.assert_called_once_with(Default.id == 1)
        mock_query.return_value.filter.return_value.one_or_none.assert_called_once()
        mock_merge.assert_called_once_with(Default(id=1, name="new_default"))
        mock_commit.assert_called_once()

    @patch('openapi_server.config_test.db.session.query')
    def test_update_default_not_found(self, mock_query):
        mock_query.return_value.filter.return_value.one_or_none.return_value = None
        with self.assertRaisesRegex(Exception, "Default with ID: 0 not found"):
            result = DefaultService.update_default(Default_schema.dump(Default(id=0, name="default")))

    @patch('openapi_server.config_test.db.session.delete')
    @patch('openapi_server.config_test.db.session.commit')
    @patch('openapi_server.config_test.db.session.query')
    def test_delete_default(self, mock_query, mock_commit, mock_delete):
        mock_query.return_value.filter.return_value.one_or_none.return_value = Default(id=1, name="default")
        mock_commit.return_value = None
        expected_result = "Default with ID: 1 successfully deleted"
        result = DefaultService.delete_default(1)
        self.assertEqual(result, expected_result)
        mock_query.assert_called_once_with(Default)
        mock_query.return_value.filter.assert_called_once_with(Default.id == 1)
        mock_query.return_value.filter.return_value.one_or_none.assert_called_once()
        mock_delete.assert_called_once_with(Default(id=1, name="default"))
        mock_commit.assert_called_once()

    @patch('openapi_server.config_test.db.session.query')
    def test_delete_default_not_found(self, mock_query):
        mock_query.return_value.filter.return_value.one_or_none.return_value = None
        with self.assertRaisesRegex(Exception, "Default with ID: 0 not found"):
            result = DefaultService.delete_default(0)