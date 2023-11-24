from python-flask-server.openapi_server.services.pagination_sorting import *
import unittest
from unittest.mock import patch
from openapi_server.utils.constants import *
from openapi_server.services.searching import searching
from app import app

class TestPaginationSorting(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_pagination_sorting(self):
        with patch('flask.request') as mock_request:
            mock_request.args.get.return_value = 1
            response = self.app.get('/pagination_sorting')
            self.assertEqual(response.status_code, 200)

    def test_pagination_sorting_sorting_desc(self):
        with patch('flask.request') as mock_request:
            mock_request.args.get.side_effect = [1, 10, 'name', 'desc']
            response = self.app.get('/pagination_sorting')
            self.assertEqual(response.status_code, 200)

    def test_pagination_sorting_sorting_asc(self):
        with patch('flask.request') as mock_request:
            mock_request.args.get.side_effect = [1, 10, 'name', 'asc']
            response = self.app.get('/pagination_sorting')
            self.assertEqual(response.status_code, 200)

    def test_pagination_sorting_search_params(self):
        with patch('flask.request') as mock_request:
            mock_request.args.get.side_effect = [1, 10, 'name', 'desc', 'search_params']
            with patch('openapi_server.services.searching.searching') as mock_searching:
                mock_searching.return_value = True
                response = self.app.get('/pagination_sorting')
                self.assertEqual(response.status_code, 200)
                mock_searching.assert_called_once()

if __name__ == '__main__':
    unittest.main()