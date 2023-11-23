from python-flask-server.openapi_server.utils.constants import *
import unittest

class TestPagination(unittest.TestCase):
    def test_default_values(self):
        self.assertEqual(pageNumber, 1)
        self.assertEqual(pageSize, 100)
        self.assertEqual(sortBy, 'id')
        self.assertEqual(sortDir, 'asc')
        self.assertEqual(search, '')
        
    def test_parameter_values(self):
        global pageNumber, pageSize, sortBy, sortDir, search
        
        pageNumber = 2
        self.assertEqual(pageNumber, 2)
        
        pageSize = 50
        self.assertEqual(pageSize, 50)
        
        sortBy = 'name'
        self.assertEqual(sortBy, 'name')
        
        sortDir = 'desc'
        self.assertEqual(sortDir, 'desc')
        
        search = 'test'
        self.assertEqual(search, 'test')
        
    def test_invalid_parameter(self):
        global pageNumber, pageSize, sortBy, sortDir, search
        
        with self.assertRaises(NameError):
            PARAM_PAGE_NUMBER = 'invalid'
            pageNumber = PARAM_PAGE_NUMBER
        
        with self.assertRaises(NameError):
            PARAM_PAGE_SIZE = 'invalid'
            pageSize = PARAM_PAGE_SIZE
        
        with self.assertRaises(NameError):
            PARAM_SORT_BY = 'invalid'
            sortBy = PARAM_SORT_BY
        
        with self.assertRaises(NameError):
            PARAM_SORT_DIR = 'invalid'
            sortDir = PARAM_SORT_DIR
        
        with self.assertRaises(NameError):
            PARAM_SEARCH = 'invalid'
            search = PARAM_SEARCH
        
if __name__ == '__main__':
    unittest.main()