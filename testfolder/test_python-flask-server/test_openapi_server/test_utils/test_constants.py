from python-flask-server.openapi_server.utils.constants import *
import unittest

class TestDefaultParameters(unittest.TestCase):
    def test_pageNumber(self):
        self.assertEqual(pageNumber, 1)
        
    def test_pageSize(self):
        self.assertEqual(pageSize, 100)
        
    def test_sortBy(self):
        self.assertEqual(sortBy, 'id')
        
    def test_sortDir(self):
        self.assertEqual(sortDir, 'asc')
        
    def test_search(self):
        self.assertEqual(search, '')

class TestParameters(unittest.TestCase):
    def test_PARAM_PAGE_NUMBER(self):
        self.assertEqual(PARAM_PAGE_NUMBER, 'pageNumber')
        
    def test_PARAM_PAGE_SIZE(self):
        self.assertEqual(PARAM_PAGE_SIZE, 'pageSize')
        
    def test_PARAM_SORT_BY(self):
        self.assertEqual(PARAM_SORT_BY, 'sortBy')
        
    def test_PARAM_SORT_DIR(self):
        self.assertEqual(PARAM_SORT_DIR, 'sortDir')
        
    def test_PARAM_SEARCH(self):
        self.assertEqual(PARAM_SEARCH, 'search')