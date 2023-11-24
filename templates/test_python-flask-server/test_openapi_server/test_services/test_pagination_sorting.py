from python-flask-server.openapi_server.services.pagination_sorting import *
import unittest
from unittest.mock import patch
from flask import Flask, request
from openapi_server.utils.constants import *
from openapi_server.services.searching import searching
from file_name import pagination_sorting

class TestPaginationSorting(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)

    def test_pagination_sorting(self):
        with self.app.test_request_context('/?page_number=1&page_size=10&sort_by=id&sort_dir=asc&search=test'):
            result = pagination_sorting(Model)
            self.assertIsInstance(result, list)
            self.assertGreaterEqual(len(result), 0)
            self.assertEqual(result[0]['id'], 1)

    def test_pagination_sorting_default(self):
        with self.app.test_request_context('/'):
            result = pagination_sorting(Model)
            self.assertIsInstance(result, list)
            self.assertGreaterEqual(len(result), 0)

    def test_pagination_sorting_sort_desc(self):
        with self.app.test_request_context('/?sort_dir=desc&sort_by=id'):
            result = pagination_sorting(Model)
            self.assertIsInstance(result, list)
            self.assertGreaterEqual(len(result), 0)
            self.assertEqual(result[0]['id'], 100)

    def test_pagination_sorting_search(self):
        with self.app.test_request_context('/?search=apple'):
            result = pagination_sorting(Model)
            self.assertIsInstance(result, list)
            self.assertGreaterEqual(len(result), 0)
            self.assertTrue('apple' in result[0]['name'])

    def test_pagination_sorting_wrong_values(self):
        with self.app.test_request_context('/?page_number=-1&page_size=-1&sort_by=wrong&sort_dir=wrong'):
            result = pagination_sorting(Model)
            self.assertIsInstance(result, list)
            self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()