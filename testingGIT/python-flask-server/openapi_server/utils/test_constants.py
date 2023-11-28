from constants import *
import unittest

class TestParameters(unittest.TestCase):
    
    def test_default_pageNumber(self):
        self.assertEqual(pageNumber, 1, "Default pageNumber should be 1")
    
    def test_default_pageSize(self):
        self.assertEqual(pageSize, 100, "Default pageSize should be 100")
        
    def test_default_sortBy(self):
        self.assertEqual(sortBy, 'id', "Default sortBy should be 'id'")
        
    def test_default_sortDir(self):
        self.assertEqual(sortDir, 'asc', "Default sortDir should be 'asc'")
        
    def test_default_search(self):
        self.assertEqual(search, '', "Default search should be an empty string")
        
    def test_custom_pageNumber(self):
        custom_pageNumber = 2
        self.assertEqual(custom_pageNumber, 2, "Custom pageNumber should be 2")
        
    def test_custom_pageSize(self):
        custom_pageSize = 50
        self.assertEqual(custom_pageSize, 50, "Custom pageSize should be 50")
        
    def test_custom_sortBy(self):
        custom_sortBy = 'name'
        self.assertEqual(custom_sortBy, 'name', "Custom sortBy should be 'name'")
        
    def test_custom_sortDir(self):
        custom_sortDir = 'desc'
        self.assertEqual(custom_sortDir, 'desc', "Custom sortDir should be 'desc'")
        
    def test_custom_search(self):
        custom_search = 'test'
        self.assertEqual(custom_search, 'test', "Custom search should be 'test'")