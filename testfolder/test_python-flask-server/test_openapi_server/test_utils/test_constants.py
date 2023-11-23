from python-flask-server.openapi_server.utils.constants import *
import unittest
from my_module import my_function

class TestMyFunction(unittest.TestCase):
    def test_default_parameters(self):
        result = my_function()
        self.assertEqual(result['pageNumber'], 1)
        self.assertEqual(result['pageSize'], 100)
        self.assertEqual(result['sortBy'], 'id')
        self.assertEqual(result['sortDir'], 'asc')
        self.assertEqual(result['search'], '')

    def test_custom_parameters(self):
        result = my_function(
            pageNumber=2,
            pageSize=50,
            sortBy='name',
            sortDir='desc',
            search='example'
        )
        self.assertEqual(result['pageNumber'], 2)
        self.assertEqual(result['pageSize'], 50)
        self.assertEqual(result['sortBy'], 'name')
        self.assertEqual(result['sortDir'], 'desc')
        self.assertEqual(result['search'], 'example')

    def test_missing_parameters(self):
        result = my_function(
            PARAM_PAGE_NUMBER=2,
            PARAM_PAGE_SIZE=50,
            PARAM_SORT_BY='name'
        )
        self.assertEqual(result['pageNumber'], 2)
        self.assertEqual(result['pageSize'], 50)
        self.assertEqual(result['sortBy'], 'name')
        self.assertEqual(result['sortDir'], 'asc')
        self.assertEqual(result['search'], '')

    def test_invalid_parameters(self):
        with self.assertRaises(ValueError):
            my_function(pageNumber=0)
        
        with self.assertRaises(ValueError):
            my_function(pageSize=0)
        
        with self.assertRaises(ValueError):
            my_function(sortDir='invalid')

if __name__ == '__main__':
    unittest.main()