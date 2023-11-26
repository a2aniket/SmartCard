from python-flask-server.openapi_server.services.pagination_sorting import *
import unittest
from unittest.mock import Mock, patch
from flask import Flask, request
from openapi_server.utils.constants import *
from openapi_server.services.searching import searching
from file_with_code_snippet import pagination_sorting

class TestPaginationSorting(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        
    def tearDown(self):
        self.app_context.pop()
        
    def test_pagination_sorting(self):
        with patch('flask.request') as mock_request:
            mock_request.args.get.side_effect = lambda x,default,type: {
                PARAM_PAGE_NUMBER: 2,
                PARAM_PAGE_SIZE: 10,
                PARAM_SORT_BY: "name",
                PARAM_SORT_DIR: "asc"
            }.get(x,default)
            
            mock_searching = Mock()
            mock_searching.return_value = "query object"
            with patch('file_with_code_snippet.searching', mock_searching):
                with patch.object(Mock(), 'desc') as mock_desc:
                    with patch.object(Mock(), 'asc') as mock_asc:
                        mock_desc.return_value = "desc object"
                        mock_asc.return_value = "asc object"
                        result = pagination_sorting(Mock())
                        self.assertEqual(result, "query items")
                        mock_searching.assert_called_once_with(None, Mock())
                        mock_desc.assert_not_called()
                        mock_asc.assert_called_once()
                        
    def test_pagination_sorting_with_desc_sorting(self):
        with patch('flask.request') as mock_request:
            mock_request.args.get.side_effect = lambda x,default,type: {
                PARAM_PAGE_NUMBER: 2,
                PARAM_PAGE_SIZE: 10,
                PARAM_SORT_BY: "name",
                PARAM_SORT_DIR: "desc"
            }.get(x,default)
            
            mock_searching = Mock()
            mock_searching.return_value = "query object"
            with patch('file_with_code_snippet.searching', mock_searching):
                with patch.object(Mock(), 'desc') as mock_desc:
                    with patch.object(Mock(), 'asc') as mock_asc:
                        mock_desc.return_value = "desc object"
                        mock_asc.return_value = "asc object"
                        result = pagination_sorting(Mock())
                        self.assertEqual(result, "query items")
                        mock_searching.assert_called_once_with(None, Mock())
                        mock_desc.assert_called_once()
                        mock_asc.assert_not_called()
                        
    def test_pagination_sorting_with_search_params(self):
        with patch('flask.request') as mock_request:
            mock_request.args.get.side_effect = lambda x,default,type: {
                PARAM_PAGE_NUMBER: 2,
                PARAM_PAGE_SIZE: 10,
                PARAM_SORT_BY: "name",
                PARAM_SORT_DIR: "asc",
                "search": "search params"
            }.get(x,default)
            
            mock_searching = Mock()
            mock_searching.return_value = "query object"
            with patch('file_with_code_snippet.searching', mock_searching):
                with patch.object(Mock(), 'desc') as mock_desc:
                    with patch.object(Mock(), 'asc') as mock_asc:
                        mock_desc.return_value = "desc object"
                        mock_asc.return_value = "asc object"
                        result = pagination_sorting(Mock())
                        self.assertEqual(result, "query items")
                        mock_searching.assert_called_once_with("search params", Mock())
                        mock_desc.assert_not_called()
                        mock_asc.assert_called_once()
                        
if __name__ == '__main__':
    unittest.main()