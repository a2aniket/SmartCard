from services.pagination_sorting import *
import unittest
from flask import Flask
from openapi_server.utils.constants import *
from openapi_server.services.searching import searching
from openapi_server.app import pagination_sorting

class TestPaginationSorting(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)

    def test_pagination_sorting(self):
        with self.app.test_request_context('/?page_number=1&page_size=10&sort_by=id&sort_dir=asc'):
            result = pagination_sorting(Model)
            self.assertEqual(len(result), 10)
            self.assertEqual(result[0]['id'], 1)
            self.assertEqual(result[-1]['id'], 10)
            
        with self.app.test_request_context('/?page_number=2&page_size=10&sort_by=id&sort_dir=asc'):
            result = pagination_sorting(Model)
            self.assertEqual(len(result), 10)
            self.assertEqual(result[0]['id'], 11)
            self.assertEqual(result[-1]['id'], 20)
            
        with self.app.test_request_context('/?page_number=1&page_size=10&sort_by=name&sort_dir=desc'):
            result = pagination_sorting(Model)
            self.assertEqual(len(result), 10)
            self.assertEqual(result[0]['name'], 'Zoe')
            self.assertEqual(result[-1]['name'], 'Alice')
            
        with self.app.test_request_context('/?search=John'):
            result = pagination_sorting(Model)
            self.assertEqual(len(result), 2)
            self.assertEqual(result[0]['name'], 'John')
            self.assertEqual(result[1]['name'], 'Johnny')
            
        with self.app.test_request_context('/?search=John&page_number=2&page_size=1&sort_by=id&sort_dir=asc'):
            result = pagination_sorting(Model)
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]['name'], 'Johnny')
            self.assertEqual(result[0]['id'], 2)