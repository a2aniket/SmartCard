from python-flask-server.openapi_server.services.pagination_sorting import *
import unittest
from unittest.mock import Mock, patch
from flask import Flask, request
from openapi_server.utils.constants import *
from openapi_server.services.searching import searching
from openapi_server import pagination_sorting

class TestPaginationSorting(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)

    def test_pagination_sorting(self):
        with self.app.test_request_context('/'):
            # Set up mock values for request arguments
            request.args = Mock()
            request.args.get.side_effect = lambda x, default, type: {
                PARAM_PAGE_NUMBER: 2,
                PARAM_PAGE_SIZE: 10,
                PARAM_SORT_BY: 'name',
                PARAM_SORT_DIR: 'asc'
            }.get(x, default)

            # Set up mock values for constants
            pageNumber = 1
            pageSize = 20
            sortBy = 'id'
            sortDir = 'desc'

            # Set up mock values for Model and search_params
            Model = Mock()
            search_params = 'test'

            # Set up mock values for query object and items
            query = Mock()
            query.items = [{'id': 1, 'name': 'test1'}, {'id': 2, 'name': 'test2'}]

            # Patch the searching function to return a query object
            with patch('openapi_server.services.searching.searching') as mock_searching:
                mock_searching.return_value = q = Mock()
                q.order_by.return_value = sorted = Mock()
                sorted.desc.return_value = 'desc'
                sorted.asc.return_value = 'asc'
                q.paginate.return_value = query

                # Call the pagination_sorting function and check the results
                result = pagination_sorting(Model)
                self.assertEqual(result, [{'id': 1, 'name': 'test1'}, {'id': 2, 'name': 'test2'}])

if __name__ == '__main__':
    unittest.main()