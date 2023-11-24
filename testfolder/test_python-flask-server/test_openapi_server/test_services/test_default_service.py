from python-flask-server.openapi_server.services.default_service import *
import unittest
from unittest.mock import Mock, patch
from openapi_server.services.default_service import DefaultService


class TestDefaultService(unittest.TestCase):

    @patch('openapi_server.services.default_service.Default.query')
    def test_get_default_list_success(self, mock_query):
        mock_default = Mock()
        mock_default.id = 1
        mock_default.name = "default"

        mock_query.filter_by.return_value.order_by.return_value.paginate.return_value.items = [mock_default]

        result = DefaultService.get_default_list()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['id'], 1)
        self.assertEqual(result[0]['name'], 'default')

    @patch('openapi_server.services.default_service.abort')
    @patch('openapi_server.services.default_service.Default.query')
    def test_get_default_list_no_defaults(self, mock_query, mock_abort):
        mock_query.filter_by.return_value.order_by.return_value.paginate.return_value.items = []

        DefaultService.get_default_list()

        mock_abort.assert_called_with(404, "No default found")

    @patch('openapi_server.services.default_service.Default.query')
    def test_get_default_success(self, mock_query):
        mock_default = Mock()
        mock_default.id = 1
        mock_default.name = "default"

        mock_query.filter.return_value.one_or_none.return_value = mock_default

        result = DefaultService.get_default(1)

        self.assertEqual(result['id'], 1)
        self.assertEqual(result['name'], 'default')

    @patch('openapi_server.services.default_service.abort')
    @patch('openapi_server.services.default_service.Default.query')
    def test_get_default_invalid_id(self, mock_query, mock_abort):
        result = DefaultService.get_default(-1)

        mock_abort.assert_called_with(404, "Default with ID: -1 does not exist")

    @patch('openapi_server.services.default_service.abort')
    @patch('openapi_server.services.default_service.Default.query')
    def test_get_default_not_found(self, mock_query, mock_abort):
        mock_query.filter.return_value.one_or_none.return_value = None

        DefaultService.get_default(1)

        mock_abort.assert_called_with(404, "Default with ID: 1 does not exist")

    @patch('openapi_server.services.default_service.Default.query')
    def test_add_default_success(self, mock_query):
        mock_default = {'id': 1, 'name': 'default'}

        mock_query.filter.return_value.one_or_none.return_value = None

        result = DefaultService.add_default(mock_default)

        self.assertEqual(result['id'], 1)
        self.assertEqual(result['name'], 'default')

    @patch('openapi_server.services.default_service.abort')
    @patch('openapi_server.services.default_service.Default.query')
    def test_add_default_already_exists(self, mock_query, mock_abort):
        mock_default = {'id': 1, 'name': 'default'}

        mock_query.filter.return_value.one_or_none.return_value = Mock()

        DefaultService.add_default(mock_default)

        mock_abort.assert_called_with(400, "Default with ID: 1 already exists")

    @patch('openapi_server.services.default_service.Default.query')
    def test_update_default_success(self, mock_query):
        mock_default = {'id': 1, 'name': 'default'}

        mock_query.filter.return_value.one_or_none.return_value = Mock()

        result = DefaultService.update_default(mock_default)

        self.assertEqual(result['id'], 1)
        self.assertEqual(result['name'], 'default')

    @patch('openapi_server.services.default_service.abort')
    @patch('openapi_server.services.default_service.Default.query')
    def test_update_default_not_found(self, mock_query, mock_abort):
        mock_default = {'id': 1, 'name': 'default'}

        mock_query.filter.return_value.one_or_none.return_value = None

        DefaultService.update_default(mock_default)

        mock_abort.assert_called_with(404, "Default with ID: 1 not found")

    @patch('openapi_server.services.default_service.Default.query')
    def test_delete_default_success(self, mock_query):
        mock_query.filter.return_value.one_or_none.return_value = Mock()

        result = DefaultService.delete_default(1)

        self.assertEqual(result, 'Default with ID: 1 successfully deleted')

    @patch('openapi_server.services.default_service.abort')
    @patch('openapi_server.services.default_service.Default.query')
    def test_delete_default_not_found(self, mock_query, mock_abort):
        mock_query.filter.return_value.one_or_none.return_value = None

        DefaultService.delete_default(1)

        mock_abort.assert_called_with(400, "Default with ID: 1 not found")