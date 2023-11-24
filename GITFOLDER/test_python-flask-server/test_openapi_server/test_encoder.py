from python-flask-server.openapi_server.encoder import *
import unittest
from openapi_server.models.base_model_ import Model
from unittest.mock import MagicMock
from json import dumps
from json.decoder import JSONDecodeError

class TestJSONEncoder(unittest.TestCase):
    def test_default_with_model(self):
        model = Model()
        model.openapi_types = {
            "attr1": str,
            "attr2": int
        }
        model.attribute_map = {
            "attr1": "attribute1",
            "attr2": "attribute2"
        }
        model.attr1 = "test"
        model.attr2 = 123
        json_encoder = JSONEncoder()
        result = json_encoder.default(model)
        expected_result = {
            "attribute1": "test",
            "attribute2": 123
        }
        self.assertEqual(result, expected_result)

    def test_default_without_model(self):
        obj = MagicMock()
        obj.return_value = "test"
        json_encoder = JSONEncoder()
        result = json_encoder.default(obj)
        expected_result = "test"
        self.assertEqual(result, expected_result)

    def test_encode_model(self):
        model = Model()
        model.openapi_types = {
            "attr1": str,
            "attr2": int
        }
        model.attribute_map = {
            "attr1": "attribute1",
            "attr2": "attribute2"
        }
        model.attr1 = "test"
        model.attr2 = 123
        json_encoder = JSONEncoder()
        result = json_encoder.encode(model)
        expected_result = dumps({
            "attribute1": "test",
            "attribute2": 123
        })
        self.assertEqual(result, expected_result)

    def test_encode_non_model(self):
        obj = MagicMock()
        obj.return_value = "test"
        json_encoder = JSONEncoder()
        result = json_encoder.encode(obj)
        expected_result = dumps("test")
        self.assertEqual(result, expected_result)

    def test_decode(self):
        json_str = dumps({"attr1": "test", "attr2": 123})
        json_encoder = JSONEncoder()
        result = json_encoder.decode(json_str)
        expected_result = {
            "attr1": "test",
            "attr2": 123
        }
        self.assertEqual(result, expected_result)

    def test_decode_with_error(self):
        json_str = "invalid json string"
        json_encoder = JSONEncoder()
        with self.assertRaises(JSONDecodeError):
            json_encoder.decode(json_str)