from python-flask-server.openapi_server.services.pagination_sorting import *
import unittest
from unittest.mock import Mock
from openapi_server import pagination_sorting

class TestPaginationSorting(unittest.TestCase):

    def test_pagination_sorting(self):
        # Set up mock request object
        mock_request = Mock()
        mock_request.args.get.side_effect = lambda x, default=None, type=None: {
            'page_number': 1,
            'page_size': 10,
            'sort_by': 'id',
            'sort_dir': 'asc',
            'search': ''
        }.get(x, default)

        # Call the pagination_sorting function with the mock request and model
        result = pagination_sorting(mock_request, Mock())

        # Assert that the result is a list of dicts with length 10
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIsInstance(result[0], dict)

if __name__ == '__main__':
    unittest.main()