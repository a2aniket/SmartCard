from python-flask-server.openapi_server.encoder import *
import unittest
from openapi_server.models.base_model_ import Model
from unittest.mock import MagicMock

class TestJSONEncoder(unittest.TestCase):

    def setUp(self):
        self.encoder = JSONEncoder()
        self.model = Model()

    def test_default(self):
        obj = {"test": "test_value"}
        result = self.encoder.default(obj)
        self.assertEqual(result, obj)

    def test_default_model(self):
        self.model.openapi_types = {"attr": str}
        self.model.attribute_map = {"attr": "attr"}
        self.model.attr = "test_value"
        result = self.encoder.default(self.model)
        self.assertEqual(result, {"attr": "test_value"})

    def test_default_model_include_nulls(self):
        self.encoder.include_nulls = True
        self.model.openapi_types = {"attr": str}
        self.model.attribute_map = {"attr": "attr"}
        self.model.attr = None
        result = self.encoder.default(self.model)
        self.assertEqual(result, {"attr": None})

    def test_default_model_exclude_nulls(self):
        self.encoder.include_nulls = False
        self.model.openapi_types = {"attr": str}
        self.model.attribute_map = {"attr": "attr"}
        self.model.attr = None
        result = self.encoder.default(self.model)
        self.assertEqual(result, {})

if __name__ == '__main__':
    unittest.main()