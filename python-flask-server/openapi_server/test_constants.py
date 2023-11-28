from utils.constants import *
import unittest

class TestParameters(unittest.TestCase):
    
    def test_default_pageNumber(self):
        self.assertEqual(pageNumber, 1)
        
    def test_default_pageSize(self):
        self.assertEqual(pageSize, 100)
        
    def test_default_sortBy(self):
        self.assertEqual(sortBy, 'id')
        
    def test_default_sortDir(self):
        self.assertEqual(sortDir, 'asc')
        
    def test_default_search(self):
        self.assertEqual(search, '')
        
    def test_custom_pageNumber(self):
        custom_pageNumber = 5
        self.assertEqual(custom_pageNumber, 5)
        
    def test_custom_pageSize(self):
        custom_pageSize = 50
        self.assertEqual(custom_pageSize, 50)
        
    def test_custom_sortBy(self):
        custom_sortBy = 'name'
        self.assertEqual(custom_sortBy, 'name')
        
    def test_custom_sortDir(self):
        custom_sortDir = 'desc'
        self.assertEqual(custom_sortDir, 'desc')
        
    def test_custom_search(self):
        custom_search = 'example'
        self.assertEqual(custom_search, 'example')
        
if __name__ == '__main__':
    unittest.main()