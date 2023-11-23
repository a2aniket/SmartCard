from python-flask-server.openapi_server.utils.constants import *
import unittest

class TestPagination(unittest.TestCase):
    def test_default_parameters(self):
        self.assertEqual(pageNumber, 1)
        self.assertEqual(pageSize, 100)
        self.assertEqual(sortBy, 'id')
        self.assertEqual(sortDir, 'asc')
        self.assertEqual(search, '')

    def test_custom_parameters(self):
        custom_pageNumber = 2
        custom_pageSize = 50
        custom_sortBy = 'name'
        custom_sortDir = 'desc'
        custom_search = 'example'

        self.assertEqual(custom_pageNumber, 2)
        self.assertEqual(custom_pageSize, 50)
        self.assertEqual(custom_sortBy, 'name')
        self.assertEqual(custom_sortDir, 'desc')
        self.assertEqual(custom_search, 'example')

    def test_missing_parameters(self):
        self.assertRaises(TypeError, function_name)

    def test_invalid_parameters(self):
        invalid_pageNumber = 'invalid'
        invalid_pageSize = 'invalid'
        invalid_sortBy = 123
        invalid_sortDir = True
        invalid_search = None

        self.assertRaises(TypeError, function_name, invalid_pageNumber, pageSize, sortBy, sortDir, search)
        self.assertRaises(TypeError, function_name, pageNumber, invalid_pageSize, sortBy, sortDir, search)
        self.assertRaises(TypeError, function_name, pageNumber, pageSize, invalid_sortBy, sortDir, search)
        self.assertRaises(TypeError, function_name, pageNumber, pageSize, sortBy, invalid_sortDir, search)
        self.assertRaises(TypeError, function_name, pageNumber, pageSize, sortBy, sortDir, invalid_search)

if __name__ == '__main__':
    unittest.main()