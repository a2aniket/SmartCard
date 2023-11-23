from python-flask-server.openapi_server.services.pagination_sorting import *
import unittest
from flask import Flask
from openapi_server.utils.constants import *
from openapi_server.services.searching import searching
from unittest.mock import patch, MagicMock

app = Flask(__name__)

class TestPaginationSorting(unittest.TestCase):
    
    @patch('flask.request')
    def test_pagination_sorting(self, mock_request):
        mock_request.args.get.side_effect = lambda x, default, type: {
            PARAM_PAGE_NUMBER: 2,
            PARAM_PAGE_SIZE: 10,
            PARAM_SORT_BY: 'id',
            PARAM_SORT_DIR: 'desc'
        }.get(x, default)
        
        class Model:
            id = MagicMock()
        
        search_params = 'test'
        q = searching(search_params, Model)
        q.order_by = MagicMock()
        q.paginate = MagicMock()
        
        pagination_sorting(Model)
        
        q.order_by.assert_called_once_with(getattr(Model, 'id').desc())
        q.paginate.assert_called_once_with(page=2, per_page=10)