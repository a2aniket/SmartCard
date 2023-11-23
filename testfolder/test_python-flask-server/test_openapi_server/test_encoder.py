from python-flask-server.openapi_server.encoder import *
import unittest
from unittest.mock import Mock
from openapi_server.models.base_model_ import Model
from your_module import JSONEncoder

class TestJSONEncoder(unittest.TestCase):

    def setUp(self):
        self.json_encoder = JSONEncoder()

    def test_default_for_model(self):
        mock_model = Mock(spec=Model)
        mock_model.openapi_types = {'attr1': int, 'attr2': str}
        mock_model.attribute_map = {'attr1': 'attribute1', 'attr2': 'attribute2'}
        mock_model.attr1 = 1
        mock_model.attr2 = 'test'
        expected_output = {'attribute1': 1, 'attribute2': 'test'}
        self.assertEqual(self.json_encoder.default(mock_model), expected_output)

    def test_default_for_non_model(self):
        non_model_input = {'key': 'value'}
        expected_output = '{"key": "value"}'
        self.assertEqual(self.json_encoder.default(non_model_input), expected_output)

    def test_default_with_nulls(self):
        self.json_encoder.include_nulls = True
        mock_model = Mock(spec=Model)
        mock_model.openapi_types = {'attr1': int, 'attr2': str}
        mock_model.attribute_map = {'attr1': 'attribute1', 'attr2': 'attribute2'}
        mock_model.attr1 = None
        mock_model.attr2 = 'test'
        expected_output = {'attribute1': None, 'attribute2': 'test'}
        self.assertEqual(self.json_encoder.default(mock_model), expected_output)

    def test_default_without_nulls(self):
        self.json_encoder.include_nulls = False
        mock_model = Mock(spec=Model)
        mock_model.openapi_types = {'attr1': int, 'attr2': str}
        mock_model.attribute_map = {'attr1': 'attribute1', 'attr2': 'attribute2'}
        mock_model.attr1 = None
        mock_model.attr2 = 'test'
        expected_output = {'attribute2': 'test'}
        self.assertEqual(self.json_encoder.default(mock_model), expected_output)

if __name__ == '__main__':
    unittest.main()