from python-flask-server.openapi_server.utils.constants import *
import unittest

class TestCodeSnippet(unittest.TestCase):
    def test_default_parameters(self):
        self.assertEqual(pageNumber, 1)
        self.assertEqual(pageSize, 100)
        self.assertEqual(sortBy, 'id')
        self.assertEqual(sortDir, 'asc')
        self.assertEqual(search, '')
        
    def test_set_parameters(self):
        global pageNumber, pageSize, sortBy, sortDir, search
        pageNumber = 2
        pageSize = 50
        sortBy = 'name'
        sortDir = 'desc'
        search = 'test'
        self.assertEqual(pageNumber, 2)
        self.assertEqual(pageSize, 50)
        self.assertEqual(sortBy, 'name')
        self.assertEqual(sortDir, 'desc')
        self.assertEqual(search, 'test')
        
    def test_param_names(self):
        self.assertEqual(PARAM_PAGE_NUMBER, 'pageNumber')
        self.assertEqual(PARAM_PAGE_SIZE, 'pageSize')
        self.assertEqual(PARAM_SORT_BY, 'sortBy')
        self.assertEqual(PARAM_SORT_DIR, 'sortDir')
        self.assertEqual(PARAM_SEARCH, 'search')