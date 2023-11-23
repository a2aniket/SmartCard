from python-flask-server.openapi_server.services.pagination_sorting import *
import unittest
from flask import Flask

class TestPaginationSorting(unittest.TestCase):
    
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_pagination_sorting(self):
        response = self.client.get('/pagination_sorting?page_number=1&page_size=10&sort_by=id&sort_dir=asc')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        self.assertLessEqual(len(response.json), 10)
        self.assertTrue(all(isinstance(item, dict) for item in response.json))
        self.assertTrue(all('id' in item for item in response.json))

    def test_pagination_sorting_invalid_sort_dir(self):
        response = self.client.get('/pagination_sorting?page_number=1&page_size=10&sort_by=id&sort_dir=invalid')
        self.assertEqual(response.status_code, 400)

    def test_pagination_sorting_search_params(self):
        response = self.client.get('/pagination_sorting?page_number=1&page_size=10&sort_by=id&sort_dir=asc&search=test')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        self.assertTrue(all(isinstance(item, dict) for item in response.json))
        self.assertTrue(all('test' in item.values() for item in response.json))

    def test_pagination_sorting_invalid_page_number(self):
        response = self.client.get('/pagination_sorting?page_number=invalid&page_size=10&sort_by=id&sort_dir=asc')
        self.assertEqual(response.status_code, 400)

    def test_pagination_sorting_invalid_page_size(self):
        response = self.client.get('/pagination_sorting?page_number=1&page_size=invalid&sort_by=id&sort_dir=asc')
        self.assertEqual(response.status_code, 400)

    def test_pagination_sorting_missing_params(self):
        response = self.client.get('/pagination_sorting')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        self.assertLessEqual(len(response.json), 10)
        self.assertTrue(all(isinstance(item, dict) for item in response.json))
        self.assertTrue(all('id' in item for item in response.json))