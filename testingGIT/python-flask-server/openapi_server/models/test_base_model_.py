from base_model_ import *
import unittest
from unittest.mock import Mock

from openapi_server import util

class TestModel(unittest.TestCase):

    def setUp(self):
        self.test_dict = {'test_key': 'test_value'}
        self.mock_deserialize_model = Mock()
        util.deserialize_model = self.mock_deserialize_model

    def test_from_dict(self):
        model = util.Model.from_dict(self.test_dict)
        self.mock_deserialize_model.assert_called_with(self.test_dict, util.Model)
        self.assertEqual(model, self.mock_deserialize_model.return_value)

    def test_to_dict(self):
        model = util.Model()
        model.test_key = 'test_value'
        expected_dict = {'test_key': 'test_value'}
        self.assertEqual(model.to_dict(), expected_dict)

    def test_to_str(self):
        model = util.Model()
        model.test_key = 'test_value'
        expected_str = "{'test_key': 'test_value'}"
        self.assertEqual(model.to_str(), expected_str)

    def test_repr(self):
        model = util.Model()
        model.test_key = 'test_value'
        expected_repr = "{'test_key': 'test_value'}"
        self.assertEqual(model.__repr__(), expected_repr)

    def test_eq(self):
        model1 = util.Model()
        model2 = util.Model()
        model1.test_key = 'test_value'
        model2.test_key = 'test_value'
        self.assertEqual(model1, model2)

    def test_ne(self):
        model1 = util.Model()
        model2 = util.Model()
        model1.test_key = 'test_value1'
        model2.test_key = 'test_value2'
        self.assertNotEqual(model1, model2)