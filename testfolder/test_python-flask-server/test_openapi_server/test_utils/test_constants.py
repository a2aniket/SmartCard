from python-flask-server.openapi_server.utils.constants import *
import unittest

class TestPagination(unittest.TestCase):
    
    def test_default_parameters(self):
        self.assertEqual(pageNumber, 1)
        self.assertEqual(pageSize, 100)
        self.assertEqual(sortBy, 'id')
        self.assertEqual(sortDir, 'asc')
        self.assertEqual(search, '')
    
    def test_page_number(self):
        new_page_number = 2
        self.assertNotEqual(pageNumber, new_page_number)
        self.assertEqual(new_page_number, PARAM_PAGE_NUMBER)
    
    def test_page_size(self):
        new_page_size = 50
        self.assertNotEqual(pageSize, new_page_size)
        self.assertEqual(new_page_size, PARAM_PAGE_SIZE)
        
    def test_sort_by(self):
        new_sort_by = 'name'
        self.assertNotEqual(sortBy, new_sort_by)
        self.assertEqual(new_sort_by, PARAM_SORT_BY)
    
    def test_sort_dir(self):
        new_sort_dir = 'desc'
        self.assertNotEqual(sortDir, new_sort_dir)
        self.assertEqual(new_sort_dir, PARAM_SORT_DIR)
    
    def test_search(self):
        new_search = 'test'
        self.assertNotEqual(search, new_search)
        self.assertEqual(new_search, PARAM_SEARCH)
    
if __name__ == '__main__':
    unittest.main()