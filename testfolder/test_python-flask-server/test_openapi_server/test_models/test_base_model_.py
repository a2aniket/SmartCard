from python-flask-server.openapi_server.models.base_model_ import *
import unittest
from openapi_server import util

class TestModel(unittest.TestCase):

    def test_from_dict(self):
        # Test case when dictionary is empty
        empty_dict = {}
        model = Model.from_dict(empty_dict)
        self.assertEqual(model.__class__.__name__, 'Model')

        # Test case when dictionary has only one key-value pair
        dict_with_one_pair = {'key': 'value'}
        model = Model.from_dict(dict_with_one_pair)
        self.assertEqual(model.__class__.__name__, 'Model')

        # Test case when dictionary has multiple key-value pairs
        dict_with_multiple_pairs = {'key1': 'value1', 'key2': 'value2'}
        model = Model.from_dict(dict_with_multiple_pairs)
        self.assertEqual(model.__class__.__name__, 'Model')

    def test_to_dict(self):
        # Test case when model is empty
        model = Model()
        dict = model.to_dict()
        self.assertEqual(dict, {})

        # Test case when model has only one attribute
        model.key = 'value'
        dict = model.to_dict()
        self.assertEqual(dict, {'key': 'value'})

        # Test case when model has multiple attributes
        model.key1 = 'value1'
        model.key2 = 'value2'
        dict = model.to_dict()
        self.assertEqual(dict, {'key': 'value', 'key1': 'value1', 'key2': 'value2'})

    def test_to_str(self):
        # Test case when model is empty
        model = Model()
        string = model.to_str()
        self.assertEqual(string, '{}')

        # Test case when model has only one attribute
        model.key = 'value'
        string = model.to_str()
        self.assertEqual(string, "{'key': 'value'}")

        # Test case when model has multiple attributes
        model.key1 = 'value1'
        model.key2 = 'value2'
        string = model.to_str()
        self.assertEqual(string, "{'key': 'value', 'key1': 'value1', 'key2': 'value2'}")

    def test_eq(self):
        # Test case when two models are equal
        model1 = Model()
        model1.key = 'value'
        model2 = Model()
        model2.key = 'value'
        self.assertTrue(model1 == model2)

        # Test case when two models are not equal
        model3 = Model()
        model3.key = 'different_value'
        self.assertFalse(model1 == model3)

    def test_ne(self):
        # Test case when two models are not equal
        model1 = Model()
        model1.key = 'value'
        model2 = Model()
        model2.key = 'different_value'
        self.assertTrue(model1 != model2)

        # Test case when two models are equal
        model3 = Model()
        model3.key = 'value'
        self.assertFalse(model1 != model3)