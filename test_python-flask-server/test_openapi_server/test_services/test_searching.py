from python-flask-server.openapi_server.services.searching import *
import unittest
from unittest.mock import Mock
from my_module import searching

class TestSearching(unittest.TestCase):

    def test_searching_with_empty_params(self):
        mock_model = Mock()
        mock_model.query = Mock()
        result = searching("", mock_model)
        self.assertEqual(result, mock_model.query)

    def test_searching_with_one_criterion(self):
        mock_model = Mock()
        mock_model.query = Mock()
        mock_model.field = "field"
        mock_model.val = "val"
        search_params = "field = val"
        result = searching(search_params, mock_model)
        mock_model.query.filter.assert_called_with(mock_model.field == mock_model.val)
        self.assertEqual(result, mock_model.query.filter())

    def test_searching_with_multiple_criteria(self):
        mock_model = Mock()
        mock_model.query = Mock()
        mock_model.field1 = "field1"
        mock_model.op1 = "<"
        mock_model.val1 = 10
        mock_model.field2 = "field2"
        mock_model.op2 = "like"
        mock_model.val2 = "%test%"
        search_params = "field1 < 10;field2 like \"%test%\""
        result = searching(search_params, mock_model)
        mock_model.query.filter.assert_called_with(mock_model.field1 < mock_model.val1, mock_model.field2.like(mock_model.val2))
        self.assertEqual(result, mock_model.query.filter())

    def test_searching_with_BETWEEN_operator(self):
        mock_model = Mock()
        mock_model.query = Mock()
        mock_model.field = "field"
        mock_model.val1 = 10
        mock_model.val2 = 20
        search_params = "field BETWEEN 10AND20"
        result = searching(search_params, mock_model)
        mock_model.query.filter.assert_called_with(mock_model.field.between(mock_model.val1, mock_model.val2))
        self.assertEqual(result, mock_model.query.filter())

    def test_searching_with_invalid_operator(self):
        mock_model = Mock()
        mock_model.query = Mock()
        mock_model.field = "field"
        mock_model.val = "val"
        search_params = "field ! val"
        result = searching(search_params, mock_model)
        self.assertEqual(result, mock_model.query)

if __name__ == '__main__':
    unittest.main()