from python-flask-server.openapi_server.services.pagination_sorting import *
import unittest
from flask import Flask
from unittest.mock import patch, Mock
from openapi_server.utils.constants import *
from openapi_server.services.searching import searching
from app import pagination_sorting

class TestPaginationSorting(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_pagination_sorting(self):
        with patch('flask.request') as request:
            request.args = {
                PARAM_PAGE_NUMBER: 1,
                PARAM_PAGE_SIZE: 10,
                PARAM_SORT_BY: 'id',
                PARAM_SORT_DIR: 'asc',
                'search': 'test'
            }
            Model = Mock()
            Model.id = 1
            Model.title = 'test'
            searching.return_value.order_by.return_value.paginate.return_value.items = [Model]
            result = pagination_sorting(Model)
            self.assertEqual(result[0].id, 1)
            self.assertEqual(result[0].title, 'test')

if __name__ == '__main__':
    unittest.main()