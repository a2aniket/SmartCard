from python-flask-server.openapi_server.services.pagination_sorting import *
import unittest
from unittest.mock import Mock, patch
from openapi_server.utils.constants import *
from openapi_server.services.searching import searching
from openapi_server import app

class TestPaginationSorting(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_pagination_sorting(self):
        with patch('flask.request') as mock_request:
            mock_request.args.get.side_effect = lambda x, default, type: {
                PARAM_PAGE_NUMBER: 1,
                PARAM_PAGE_SIZE: 10,
                PARAM_SORT_BY: 'id',
                PARAM_SORT_DIR: 'desc'
            }.get(x, default)

            result = pagination_sorting(Mock())

            self.assertEqual(len(result), 10)
            self.assertEqual(result[0], 'item1')
            self.assertEqual(result[-1], 'item10')

    def test_pagination_sorting_invalid_sort_dir(self):
        with patch('flask.request') as mock_request:
            mock_request.args.get.side_effect = lambda x, default, type: {
                PARAM_PAGE_NUMBER: 1,
                PARAM_PAGE_SIZE: 10,
                PARAM_SORT_BY: 'id',
                PARAM_SORT_DIR: 'invalid_dir'
            }.get(x, default)

            result = pagination_sorting(Mock())

            self.assertEqual(len(result), 10)
            self.assertEqual(result[0], 'item1')
            self.assertEqual(result[-1], 'item10')

    def test_pagination_sorting_search_params(self):
        with patch('flask.request') as mock_request:
            mock_request.args.get.side_effect = lambda x, default, type: {
                PARAM_PAGE_NUMBER: 1,
                PARAM_PAGE_SIZE: 10,
                PARAM_SORT_BY: 'id',
                PARAM_SORT_DIR: 'asc',
                'search': 'test'
            }.get(x, default)

            with patch('openapi_server.services.searching.searching') as mock_searching:
                mock_searching.return_value = Mock(order_by=Mock().order_by)

                result = pagination_sorting(Mock())

                mock_searching.assert_called_once_with('test', Mock())
                mock_searching.return_value.order_by.assert_called_once_with(Mock().id.asc())
                self.assertEqual(len(result), 10)
                self.assertEqual(result[0], 'item1')
                self.assertEqual(result[-1], 'item10')