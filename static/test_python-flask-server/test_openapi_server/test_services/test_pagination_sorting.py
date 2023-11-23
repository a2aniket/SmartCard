from python-flask-server.openapi_server.services.pagination_sorting import *
import unittest
from unittest.mock import patch, MagicMock
from openapi_server.services.searching import searching
from openapi_server.utils.constants import *

class TestPaginationSorting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.Model = MagicMock()

    def test_pagination_sorting_default(self):
        with patch('flask.request') as mock_request:
            mock_request.args = {}
            result = pagination_sorting(self.Model)
            mock_request.args.get.assert_called_with(PARAM_PAGE_NUMBER, default=1, type=int)
            mock_request.args.get.assert_called_with(PARAM_PAGE_SIZE, default=10, type=int)
            mock_request.args.get.assert_called_with(PARAM_SORT_BY, default='id', type=str)
            mock_request.args.get.assert_called_with(PARAM_SORT_DIR, default='asc', type=str)
            self.Model.query.order_by.assert_called_with(self.Model.id.asc())
            self.Model.query.order_by().paginate.assert_called_with(page=1, per_page=10)
            self.assertEqual(result, self.Model.query.order_by().paginate().items)

    def test_pagination_sorting_custom(self):
        with patch('flask.request') as mock_request:
            mock_request.args = {
                PARAM_PAGE_NUMBER: 2,
                PARAM_PAGE_SIZE: 20,
                PARAM_SORT_BY: 'name',
                PARAM_SORT_DIR: 'desc',
                'search': 'test'
            }
            result = pagination_sorting(self.Model)
            mock_request.args.get.assert_called_with(PARAM_PAGE_NUMBER, default=1, type=int)
            mock_request.args.get.assert_called_with(PARAM_PAGE_SIZE, default=10, type=int)
            mock_request.args.get.assert_called_with(PARAM_SORT_BY, default='id', type=str)
            mock_request.args.get.assert_called_with(PARAM_SORT_DIR, default='asc', type=str)
            self.Model.query.order_by.assert_called_with(self.Model.name.desc())
            self.Model.query.order_by().paginate.assert_called_with(page=2, per_page=20)
            searching.assert_called_with('test', self.Model)
            self.assertEqual(result, self.Model.query.order_by().paginate().items)

if __name__ == '__main__':
    unittest.main()