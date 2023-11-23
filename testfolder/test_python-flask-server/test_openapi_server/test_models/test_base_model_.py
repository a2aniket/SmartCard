from python-flask-server.openapi_server.models.base_model_ import *
import unittest
from unittest.mock import MagicMock
from openapi_server import util

class TestModel(unittest.TestCase):

    def setUp(self):
        self.dikt = {'test': 'test'}
        self.model = util.deserialize_model(self.dikt, Model)

    def test_from_dict(self):
        self.assertIsInstance(self.model, Model)

    def test_to_dict(self):
        dict_obj = self.model.to_dict()
        self.assertIsInstance(dict_obj, dict)

    def test_to_str(self):
        str_obj = self.model.to_str()
        self.assertIsInstance(str_obj, str)

    def test_repr(self):
        repr_obj = self.model.__repr__()
        self.assertIsInstance(repr_obj, str)

    def test_eq(self):
        other = Model()
        other.__dict__ = self.dikt
        self.assertTrue(self.model == other)

    def test_ne(self):
        other = Model()
        self.assertTrue(self.model != other)