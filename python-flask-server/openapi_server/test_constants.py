from utils.constants import *
import unittest

class TestDefaultParams(unittest.TestCase):

    def test_default_params(self):
        self.assertEqual(pageNumber, 1)
        self.assertEqual(pageSize, 100)
        self.assertEqual(sortBy, 'id')
        self.assertEqual(sortDir, 'asc')
        self.assertEqual(search, '')

class TestParams(unittest.TestCase):

    def test_page_number(self):
        self.assertEqual(PARAM_PAGE_NUMBER, 'pageNumber')

    def test_page_size(self):
        self.assertEqual(PARAM_PAGE_SIZE, 'pageSize')

    def test_sort_by(self):
        self.assertEqual(PARAM_SORT_BY, 'sortBy')

    def test_sort_dir(self):
        self.assertEqual(PARAM_SORT_DIR, 'sortDir')

    def test_search(self):
        self.assertEqual(PARAM_SEARCH, 'search')

if __name__ == '__main__':
    unittest.main()