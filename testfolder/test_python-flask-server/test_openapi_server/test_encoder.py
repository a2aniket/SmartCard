from python-flask-server.openapi_server.encoder import *
import unittest
from openapi_server.models.base_model_ import Model
from unittest.mock import MagicMock

class TestJSONEncoder(unittest.TestCase):

    def test_default_should_return_dict(self):
        # Arrange
        json_encoder = JSONEncoder()
        model_mock = MagicMock(spec=Model)
        model_mock.openapi_types = {'attr1': 'str', 'attr2': 'int'}
        model_mock.attribute_map = {'attr1': 'attribute1', 'attr2': 'attribute2'}
        model_mock.attr1 = 'value1'
        model_mock.attr2 = 10

        # Act
        result = json_encoder.default(model_mock)

        # Assert
        expected_result = {'attribute1': 'value1', 'attribute2': 10}
        self.assertEqual(result, expected_result)

    def test_default_should_exclude_null_values(self):
        # Arrange
        json_encoder = JSONEncoder()
        model_mock = MagicMock(spec=Model)
        model_mock.openapi_types = {'attr1': 'str', 'attr2': 'int'}
        model_mock.attribute_map = {'attr1': 'attribute1', 'attr2': 'attribute2'}
        model_mock.attr1 = 'value1'
        model_mock.attr2 = None

        # Act
        result = json_encoder.default(model_mock)

        # Assert
        expected_result = {'attribute1': 'value1'}
        self.assertEqual(result, expected_result)

    def test_default_should_call_flask_encoder_if_not_model_instance(self):
        # Arrange
        json_encoder = JSONEncoder()

        # Act
        result = json_encoder.default('test')

        # Assert
        self.assertEqual(result, FlaskJSONEncoder.default(json_encoder, 'test'))

    def test_default_should_exclude_null_values_if_include_nulls_is_false(self):
        # Arrange
        json_encoder = JSONEncoder()
        json_encoder.include_nulls = False
        model_mock = MagicMock(spec=Model)
        model_mock.openapi_types = {'attr1': 'str', 'attr2': 'int'}
        model_mock.attribute_map = {'attr1': 'attribute1', 'attr2': 'attribute2'}
        model_mock.attr1 = 'value1'
        model_mock.attr2 = None

        # Act
        result = json_encoder.default(model_mock)

        # Assert
        expected_result = {'attribute1': 'value1'}
        self.assertEqual(result, expected_result)