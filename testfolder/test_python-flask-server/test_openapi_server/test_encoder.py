from python-flask-server.openapi_server.encoder import *
import unittest
from openapi_server.models.base_model_ import Model
from unittest.mock import MagicMock

class TestJSONEncoder(unittest.TestCase):

    def test_default_with_model_instance(self):
        # Arrange
        instance = Model()
        instance.openapi_types = {'test_attr': 'str'}
        instance.attribute_map = {'test_attr': 'TestAttr'}
        instance.test_attr = 'test_value'
        encoder = JSONEncoder()

        # Act
        result = encoder.default(instance)

        # Assert
        self.assertIsInstance(result, dict)
        self.assertEqual(result, {'TestAttr': 'test_value'})

    def test_default_with_non_model_instance(self):
        # Arrange
        instance = MagicMock()
        instance.return_value = 'non_model_instance'
        encoder = JSONEncoder()

        # Act
        result = encoder.default(instance)

        # Assert
        self.assertEqual(result, 'non_model_instance')

    def test_default_with_null_value(self):
        # Arrange
        instance = Model()
        instance.openapi_types = {'test_attr': 'str'}
        instance.attribute_map = {'test_attr': 'TestAttr'}
        instance.test_attr = None
        encoder = JSONEncoder()

        # Act
        result = encoder.default(instance)

        # Assert
        self.assertEqual(result, None)

    def test_default_with_include_nulls_true(self):
        # Arrange
        instance = Model()
        instance.openapi_types = {'test_attr': 'str'}
        instance.attribute_map = {'test_attr': 'TestAttr'}
        instance.test_attr = None
        encoder = JSONEncoder()
        encoder.include_nulls = True

        # Act
        result = encoder.default(instance)

        # Assert
        self.assertIsInstance(result, dict)
        self.assertEqual(result, {'TestAttr': None})