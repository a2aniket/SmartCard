from python-flask-server.openapi_server.encoder import *
import unittest
from openapi_server.models.base_model_ import Model
from unittest.mock import MagicMock

class TestJSONEncoder(unittest.TestCase):

    def setUp(self):
        self.encoder = JSONEncoder()

    def test_default_method_with_model_object(self):
        mock_model = MagicMock(spec=Model)
        mock_model.openapi_types = {'attr1': 'str', 'attr2': 'int'}
        mock_model.attribute_map = {'attr1': 'attribute1', 'attr2': 'attribute2'}
        mock_model.attr1 = 'test'
        mock_model.attr2 = 123
        expected_result = {'attribute1': 'test', 'attribute2': 123}
        self.assertEqual(self.encoder.default(mock_model), expected_result)

    def test_default_method_with_non_model_object(self):
        non_model_object = {'key1': 'value1', 'key2': 'value2'}
        expected_result = {'key1': 'value1', 'key2': 'value2'}
        self.assertEqual(self.encoder.default(non_model_object), expected_result)

    def test_default_method_with_model_object_and_null_values(self):
        mock_model = MagicMock(spec=Model)
        mock_model.openapi_types = {'attr1': 'str', 'attr2': 'int'}
        mock_model.attribute_map = {'attr1': 'attribute1', 'attr2': 'attribute2'}
        mock_model.attr1 = 'test'
        mock_model.attr2 = None
        expected_result = {'attribute1': 'test'}
        self.encoder.include_nulls = False
        self.assertEqual(self.encoder.default(mock_model), expected_result)

    def test_default_method_with_model_object_and_null_values_included(self):
        mock_model = MagicMock(spec=Model)
        mock_model.openapi_types = {'attr1': 'str', 'attr2': 'int'}
        mock_model.attribute_map = {'attr1': 'attribute1', 'attr2': 'attribute2'}
        mock_model.attr1 = 'test'
        mock_model.attr2 = None
        expected_result = {'attribute1': 'test', 'attribute2': None}
        self.encoder.include_nulls = True
        self.assertEqual(self.encoder.default(mock_model), expected_result)