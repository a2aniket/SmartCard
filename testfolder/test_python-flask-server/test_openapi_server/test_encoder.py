from python-flask-server.openapi_server.encoder import *
import unittest
from openapi_server.models.base_model_ import Model
from mock import MagicMock
from json import dumps

class TestJSONEncoder(unittest.TestCase):

    def setUp(self):
        self.encoder = JSONEncoder()

    def test_default_with_model(self):
        # Arrange
        mock_model = MagicMock(spec=Model)
        mock_model.openapi_types = {"attr1": "str", "attr2": "int"}
        mock_model.attribute_map = {"attr1": "attribute_1", "attr2": "attribute_2"}
        mock_model.attr1 = "test"
        mock_model.attr2 = 10

        # Act
        result = self.encoder.default(mock_model)

        # Assert
        expected_result = {"attribute_1": "test", "attribute_2": 10}
        self.assertEqual(result, expected_result)

    def test_default_with_non_model(self):
        # Arrange
        mock_obj = {"attr1": "test", "attr2": 10}

        # Act
        result = self.encoder.default(mock_obj)

        # Assert
        expected_result = dumps(mock_obj)
        self.assertEqual(result, expected_result)

    def test_default_with_null(self):
        # Arrange
        mock_model = MagicMock(spec=Model)
        mock_model.openapi_types = {"attr1": "str", "attr2": "int"}
        mock_model.attribute_map = {"attr1": "attribute_1", "attr2": "attribute_2"}
        mock_model.attr1 = "test"
        mock_model.attr2 = None

        # Act
        result = self.encoder.default(mock_model)

        # Assert
        expected_result = {"attribute_1": "test"}
        self.assertEqual(result, expected_result)

    def test_default_with_include_nulls(self):
        # Arrange
        self.encoder.include_nulls = True
        mock_model = MagicMock(spec=Model)
        mock_model.openapi_types = {"attr1": "str", "attr2": "int"}
        mock_model.attribute_map = {"attr1": "attribute_1", "attr2": "attribute_2"}
        mock_model.attr1 = "test"
        mock_model.attr2 = None

        # Act
        result = self.encoder.default(mock_model)

        # Assert
        expected_result = {"attribute_1": "test", "attribute_2": None}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()