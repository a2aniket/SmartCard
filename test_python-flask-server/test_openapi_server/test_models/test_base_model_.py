from python-flask-server.openapi_server.models.base_model_ import *
import unittest

class TestModel(unittest.TestCase):

    def test_from_dict(self):
        # Test case with valid dictionary input
        model_dict = {'attr1': 'value1', 'attr2': 'value2'}
        model = Model.from_dict(model_dict)
        self.assertIsInstance(model, Model)
        self.assertEqual(model.attr1, 'value1')
        self.assertEqual(model.attr2, 'value2')

        # Test case with invalid dictionary input
        model_dict = {'attr1': 'value1', 'invalid_attr': 'invalid_value'}
        with self.assertRaises(AttributeError):
            Model.from_dict(model_dict)

    def test_to_dict(self):
        # Test case with valid model input
        model = Model()
        model.attr1 = 'value1'
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['attr1'], 'value1')

        # Test case with nested model input
        nested_model = Model()
        nested_model.attr1 = 'nested_value1'
        model.attr2 = nested_model
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['attr2']['attr1'], 'nested_value1')

    def test_to_str(self):
        # Test case with valid model input
        model = Model()
        model.attr1 = 'value1'
        self.assertIsInstance(model.to_str(), str)

    def test_eq(self):
        # Test case with equal models
        model1 = Model()
        model1.attr1 = 'value1'
        model1.attr2 = 'value2'

        model2 = Model()
        model2.attr1 = 'value1'
        model2.attr2 = 'value2'

        self.assertEqual(model1, model2)

        # Test case with unequal models
        model1.attr2 = 'different_value'
        self.assertNotEqual(model1, model2)

    def test_ne(self):
        # Test case with unequal models
        model1 = Model()
        model1.attr1 = 'value1'
        model1.attr2 = 'value2'

        model2 = Model()
        model2.attr1 = 'value1'
        model2.attr2 = 'value2'

        self.assertFalse(model1 != model2)

        # Test case with equal models
        model1.attr2 = 'different_value'
        self.assertTrue(model1 != model2)