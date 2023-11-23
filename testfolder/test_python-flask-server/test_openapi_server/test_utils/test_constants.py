from python-flask-server.openapi_server.utils.constants import *
import unittest
from code_snippet import *

class TestParams(unittest.TestCase):
    
    def test_default_params(self):
        self.assertEqual(pageNumber, 1)
        self.assertEqual(pageSize, 100)
        self.assertEqual(sortBy, 'id')
        self.assertEqual(sortDir, 'asc')
        self.assertEqual(search, '')

    def test_update_params(self):
        update_params(PARAM_PAGE_NUMBER, 2)
        self.assertEqual(pageNumber, 2)

        update_params(PARAM_PAGE_SIZE, 50)
        self.assertEqual(pageSize, 50)

        update_params(PARAM_SORT_BY, 'name')
        self.assertEqual(sortBy, 'name')

        update_params(PARAM_SORT_DIR, 'desc')
        self.assertEqual(sortDir, 'desc')

        update_params(PARAM_SEARCH, 'test')
        self.assertEqual(search, 'test')

    def test_invalid_params(self):
        with self.assertRaises(ValueError):
            update_params('invalid_param', 1)

if __name__ == '__main__':
    unittest.main()