from python-flask-server.openapi_server.services.pagination_sorting import *
import unittest
from unittest.mock import MagicMock
from openapi_server.utils.constants import *
from openapi_server.services.searching import searching
from app import pagination_sorting

class TestPaginationSorting(unittest.TestCase):
    def setUp(self):
        self.Model = MagicMock()
        self.request = MagicMock()
        self.request.args.get = MagicMock(return_value=None)
        self.request.args.get.side_effect = lambda x, default=None, type=None: default

    def test_pagination_sorting_default_values(self):
        result = pagination_sorting(self.Model)
        self.assertEqual(result, [])

    def test_pagination_sorting_with_pagination_params(self):
        self.request.args.get.side_effect = lambda x, default=None, type=None: 1 if x == PARAM_PAGE_NUMBER else 10 if x == PARAM_PAGE_SIZE else default
        result = pagination_sorting(self.Model)
        self.assertEqual(result, [])

    def test_pagination_sorting_with_sorting_params(self):
        self.request.args.get.side_effect = lambda x, default=None, type=None: "name" if x == PARAM_SORT_BY else "asc" if x == PARAM_SORT_DIR else default
        result = pagination_sorting(self.Model)
        self.assertEqual(result, [])

    def test_pagination_sorting_with_search_params(self):
        self.request.args.get.side_effect = lambda x, default=None, type=None: "search query" if x == 'search' else default
        searching_mock = MagicMock(return_value=self.Model)
        searching.searching = searching_mock
        result = pagination_sorting(self.Model)
        searching_mock.assert_called_once_with("search query", self.Model)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()