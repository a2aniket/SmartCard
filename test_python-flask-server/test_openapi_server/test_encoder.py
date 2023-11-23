from python-flask-server.openapi_server.encoder import *
import unittest
from openapi_server.models.base_model_ import Model
from unittest.mock import MagicMock

class TestJSONEncoder(unittest.TestCase):
    
    def setUp(self):
        self.json_encoder = JSONEncoder()
        
    def test_default_with_model_instance(self):
        # Test if default method returns a dictionary with proper attribute mapping for model instance
        mock_model = MagicMock(spec=Model)
        mock_model.openapi_types = {'attr1': 'str', 'attr2': 'int'}
        mock_model.attribute_map = {'attr1': 'attribute_1', 'attr2': 'attribute_2'}
        mock_model.attr1 = 'value1'
        mock_model.attr2 = 2
        result = self.json_encoder.default(mock_model)
        self.assertEqual(result, {'attribute_1': 'value1', 'attribute_2': 2})
        
    def test_default_with_non_model_instance(self):
        # Test if default method returns default JSON encoding for non-model instances
        non_model_instance = {'key': 'value'}
        result = self.json_encoder.default(non_model_instance)
        self.assertEqual(result, '{"key": "value"}')
        
    def test_default_with_null_value(self):
        # Test if default method excludes null values when include_nulls is False
        mock_model = MagicMock(spec=Model)
        mock_model.openapi_types = {'attr1': 'str'}
        mock_model.attribute_map = {'attr1': 'attribute_1'}
        mock_model.attr1 = None
        result = self.json_encoder.default(mock_model)
        self.assertEqual(result, None)
        
    def test_default_with_null_value_and_include_nulls_true(self):
        # Test if default method includes null values when include_nulls is True
        self.json_encoder.include_nulls = True
        mock_model = MagicMock(spec=Model)
        mock_model.openapi_types = {'attr1': 'str'}
        mock_model.attribute_map = {'attr1': 'attribute_1'}
        mock_model.attr1 = None
        result = self.json_encoder.default(mock_model)
        self.assertEqual(result, {'attribute_1': None})
        
if __name__ == '__main__':
    unittest.main()