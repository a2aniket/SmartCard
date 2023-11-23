from python-flask-server.openapi_server.services.pagination_sorting import *
from unittest import TestCase
from unittest.mock import patch, MagicMock
from flask import Flask
from openapi_server.services.searching import searching
from openapi_server.utils.constants import *

app = Flask(__name__)

class TestPaginationSorting(TestCase):

    @patch('openapi_server.utils.constants.request')
    def test_pagination_sorting(self, mock_request):
        mock_request.args.get.side_effect = lambda x, default=None, type=None: {
            PARAM_PAGE_NUMBER: 1,
            PARAM_PAGE_SIZE: 10,
            PARAM_SORT_BY: 'name',
            PARAM_SORT_DIR: 'desc'
        }.get(x, default)

        search_params = 'test'
        Model = MagicMock()

        with patch('openapi_server.routes.pagination_sorting.searching', return_value=Model):
            with patch.object(Model, 'desc') as mock_desc:
                with patch.object(Model, 'asc') as mock_asc:
                    with patch.object(Model, 'order_by') as mock_order_by:
                        paginate_items = MagicMock()
                        paginate_items.items = [{'name': 'test1'}, {'name': 'test2'}]
                        mock_order_by.return_value = paginate_items

                        result = pagination_sorting(Model)

                        mock_desc.assert_called_with()
                        mock_order_by.assert_called_with(mock_desc.return_value)
                        self.assertEqual(result, paginate_items.items)