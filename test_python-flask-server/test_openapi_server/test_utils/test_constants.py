from python-flask-server.openapi_server.utils.constants import *
import unittest

class TestParams(unittest.TestCase):
    def test_default_params(self):
        self.assertEqual(pageNumber, 1)
        self.assertEqual(pageSize, 100)
        self.assertEqual(sortBy, 'id')
        self.assertEqual(sortDir, 'asc')
        self.assertEqual(search, '')

    def test_custom_params(self):
        custom_pageNumber = 2
        custom_pageSize = 50
        custom_sortBy = 'name'
        custom_sortDir = 'desc'
        custom_search = 'test'

        self.assertEqual(custom_pageNumber, 2)
        self.assertEqual(custom_pageSize, 50)
        self.assertEqual(custom_sortBy, 'name')
        self.assertEqual(custom_sortDir, 'desc')
        self.assertEqual(custom_search, 'test')

    def test_param_names(self):
        self.assertEqual(PARAM_PAGE_NUMBER, 'pageNumber')
        self.assertEqual(PARAM_PAGE_SIZE, 'pageSize')
        self.assertEqual(PARAM_SORT_BY, 'sortBy')
        self.assertEqual(PARAM_SORT_DIR, 'sortDir')
        self.assertEqual(PARAM_SEARCH, 'search')