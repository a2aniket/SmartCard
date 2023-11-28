from utils.constants import *
import unittest

class TestParameters(unittest.TestCase):
    def test_default_parameters(self):
        self.assertEqual(pageNumber, 1)
        self.assertEqual(pageSize, 100)
        self.assertEqual(sortBy, 'id')
        self.assertEqual(sortDir, 'asc')
        self.assertEqual(search, '')

    def test_page_number_parameter(self):
        global pageNumber
        pageNumber = 5
        self.assertEqual(pageNumber, 5)

    def test_page_size_parameter(self):
        global pageSize
        pageSize = 50
        self.assertEqual(pageSize, 50)

    def test_sort_by_parameter(self):
        global sortBy
        sortBy = 'name'
        self.assertEqual(sortBy, 'name')

    def test_sort_dir_parameter(self):
        global sortDir
        sortDir = 'desc'
        self.assertEqual(sortDir, 'desc')

    def test_search_parameter(self):
        global search
        search = 'test'
        self.assertEqual(search, 'test')

if __name__ == '__main__':
    unittest.main()