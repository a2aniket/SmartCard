from python-flask-server.openapi_server.encoder import *
import unittest
from unittest.mock import Mock
from openapi_server.models.base_model_ import Model
from your_module import JSONEncoder

class TestJSONEncoder(unittest.TestCase):
    
    def setUp(self):
        self.encoder = JSONEncoder()
        self.model_mock = Mock(spec=Model)
        self.model_mock.openapi_types = {"attr1": int, "attr2": str}
        self.model_mock.attribute_map = {"attr1": "attribute1", "attr2": "attribute2"}
        self.model_mock.attr1 = 123
        self.model_mock.attr2 = "test"
        
    def test_default_with_model(self):
        result = self.encoder.default(self.model_mock)
        expected_result = {"attribute1": 123, "attribute2": "test"}
        self.assertEqual(result, expected_result)
        
    def test_default_with_non_model(self):
        result = self.encoder.default("test")
        expected_result = "test"
        self.assertEqual(result, expected_result)
        
    def test_default_with_nulls_include_nulls_true(self):
        self.encoder.include_nulls = True
        self.model_mock.attr1 = None
        result = self.encoder.default(self.model_mock)
        expected_result = {"attribute1": None, "attribute2": "test"}
        self.assertEqual(result, expected_result)
        
    def test_default_with_nulls_include_nulls_false(self):
        self.encoder.include_nulls = False
        self.model_mock.attr1 = None
        result = self.encoder.default(self.model_mock)
        expected_result = {"attribute2": "test"}
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()