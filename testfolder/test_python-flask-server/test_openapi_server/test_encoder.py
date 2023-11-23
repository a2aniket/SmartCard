from python-flask-server.openapi_server.encoder import *
import unittest
from openapi_server.models.base_model_ import Model
from unittest.mock import MagicMock

class TestJSONEncoder(unittest.TestCase):

    def setUp(self):
        self.encoder = JSONEncoder()

    def test_default(self):
        # Test default method with non-Model object
        result = self.encoder.default("testing")
        self.assertEqual(result, FlaskJSONEncoder.default(self.encoder, "testing"))

        # Test default method with Model object
        model = Model()
        model.openapi_types = {"attr1": "str", "attr2": "bool"}
        model.attribute_map = {"attr1": "attribute1", "attr2": "attribute2"}
        model.attr1 = "test"
        model.attr2 = True

        expected_result = {"attribute1": "test", "attribute2": True}
        result = self.encoder.default(model)
        self.assertEqual(result, expected_result)

        # Test default method with Model object and include_nulls set to True
        self.encoder.include_nulls = True
        expected_result = {"attribute1": "test", "attribute2": True}
        result = self.encoder.default(model)
        self.assertEqual(result, expected_result)

        # Test default method with Model object and attribute value set to None
        model.attr1 = None
        expected_result = {"attribute2": True}
        result = self.encoder.default(model)
        self.assertEqual(result, expected_result)