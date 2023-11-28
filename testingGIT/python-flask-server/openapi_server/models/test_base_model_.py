from base_model_ import *
import unittest
from openapi_server import util

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = util.deserialize_model({"key": "value"}, Model)

    def test_from_dict(self):
        obj = Model.from_dict({"key": "value"})
        self.assertIsInstance(obj, Model)

    def test_to_dict(self):
        dikt = self.model.to_dict()
        self.assertIsInstance(dikt, dict)

    def test_to_str(self):
        string = self.model.to_str()
        self.assertIsInstance(string, str)

    def test___repr__(self):
        string = self.model.__repr__()
        self.assertIsInstance(string, str)

    def test___eq__(self):
        model2 = util.deserialize_model({"key": "value"}, Model)
        self.assertEqual(self.model, model2)

    def test___ne__(self):
        model2 = util.deserialize_model({"key": "value2"}, Model)
        self.assertNotEqual(self.model, model2)