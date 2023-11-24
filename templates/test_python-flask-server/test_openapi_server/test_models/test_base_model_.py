from python-flask-server.openapi_server.models.base_model_ import *
import unittest

class TestModel(unittest.TestCase):

    def test_from_dict(self):
        # Test for valid input
        dikt = {"attribute_1": "value_1", "attribute_2": "value_2"}
        model_obj = Model.from_dict(dikt)
        self.assertIsInstance(model_obj, Model)
        self.assertEqual(model_obj.attribute_1, "value_1")
        self.assertEqual(model_obj.attribute_2, "value_2")

        # Test for invalid input
        dikt = {"invalid_attribute": "value_1", "attribute_2": "value_2"}
        with self.assertRaises(TypeError):
            model_obj = Model.from_dict(dikt)

    def test_to_dict(self):
        # Test for valid input
        model_obj = Model()
        model_obj.attribute_1 = "value_1"
        model_obj.attribute_2 = "value_2"
        result = model_obj.to_dict()
        expected_result = {"attribute_1": "value_1", "attribute_2": "value_2"}
        self.assertEqual(result, expected_result)

        # Test for invalid input
        model_obj.attribute_3 = 10
        result = model_obj.to_dict()
        expected_result = {"attribute_1": "value_1", "attribute_2": "value_2", "attribute_3": 10}
        self.assertEqual(result, expected_result)

    def test_to_str(self):
        # Test for valid input
        model_obj = Model()
        model_obj.attribute_1 = "value_1"
        model_obj.attribute_2 = "value_2"
        result = model_obj.to_str()
        expected_result = "{'attribute_1': 'value_1', 'attribute_2': 'value_2'}"
        self.assertEqual(result, expected_result)

        # Test for invalid input
        model_obj.attribute_3 = 10
        result = model_obj.to_str()
        expected_result = "{'attribute_1': 'value_1', 'attribute_2': 'value_2', 'attribute_3': 10}"
        self.assertEqual(result, expected_result)

    def test___repr__(self):
        # Test for valid input
        model_obj = Model()
        model_obj.attribute_1 = "value_1"
        model_obj.attribute_2 = "value_2"
        result = model_obj.__repr__()
        expected_result = "{'attribute_1': 'value_1', 'attribute_2': 'value_2'}"
        self.assertEqual(result, expected_result)

        # Test for invalid input
        model_obj.attribute_3 = 10
        result = model_obj.__repr__()
        expected_result = "{'attribute_1': 'value_1', 'attribute_2': 'value_2', 'attribute_3': 10}"
        self.assertEqual(result, expected_result)

    def test___eq__(self):
        # Test for valid input
        model_obj1 = Model()
        model_obj1.attribute_1 = "value_1"
        model_obj1.attribute_2 = "value_2"

        model_obj2 = Model()
        model_obj2.attribute_1 = "value_1"
        model_obj2.attribute_2 = "value_2"

        result = model_obj1.__eq__(model_obj2)
        self.assertTrue(result)

        # Test for invalid input
        model_obj2.attribute_3 = 10
        result = model_obj1.__eq__(model_obj2)
        self.assertFalse(result)

    def test___ne__(self):
        # Test for valid input
        model_obj1 = Model()
        model_obj1.attribute_1 = "value_1"
        model_obj1.attribute_2 = "value_2"

        model_obj2 = Model()
        model_obj2.attribute_1 = "value_1"
        model_obj2.attribute_2 = "value_2"

        result = model_obj1.__ne__(model_obj2)
        self.assertFalse(result)

        # Test for invalid input
        model_obj2.attribute_3 = 10
        result = model_obj1.__ne__(model_obj2)
        self.assertTrue(result)