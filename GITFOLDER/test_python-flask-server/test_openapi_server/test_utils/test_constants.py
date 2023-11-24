from python-flask-server.openapi_server.utils.constants import *
import unittest

class TestParameter(unittest.TestCase):
    def test_default_parameters(self):
        self.assertEqual(pageNumber, 1)
        self.assertEqual(pageSize, 100)
        self.assertEqual(sortBy, 'id')
        self.assertEqual(sortDir, 'asc')
        self.assertEqual(search, '')

    def test_param_page_number(self):
        global pageNumber
        pageNumber = 2
        self.assertEqual(pageNumber, 2)

    def test_param_page_size(self):
        global pageSize
        pageSize = 50
        self.assertEqual(pageSize, 50)

    def test_param_sort_by(self):
        global sortBy
        sortBy = 'name'
        self.assertEqual(sortBy, 'name')

    def test_param_sort_dir(self):
        global sortDir
        sortDir = 'desc'
        self.assertEqual(sortDir, 'desc')

    def test_param_search(self):
        global search
        search = 'John'
        self.assertEqual(search, 'John')

if __name__ == '__main__':
    unittest.main()