from python-flask-server.openapi_server.models.base_model_ import *
import unittest

class TestModel(unittest.TestCase):

    def test_from_dict(self):
        # Test case for successful creation of model object from dictionary
        test_dict = {"attr1": "value1", "attr2": 2}
        model_obj = Model.from_dict(test_dict)
        self.assertIsInstance(model_obj, Model)

    def test_to_dict(self):
        # Test case for successful conversion of model object to dictionary
        model_obj = Model()
        model_obj.attr1 = "value1"
        model_obj.attr2 = 2
        dict_obj = model_obj.to_dict()
        self.assertIsInstance(dict_obj, dict)
        self.assertEqual(dict_obj["attr1"], "value1")
        self.assertEqual(dict_obj["attr2"], 2)

    def test_to_str(self):
        # Test case for successful conversion of model object to string
        model_obj = Model()
        model_obj.attr1 = "value1"
        model_obj.attr2 = 2
        str_obj = model_obj.to_str()
        self.assertIsInstance(str_obj, str)

    def test_eq(self):
        # Test case for successful comparison of two model objects
        model_obj1 = Model()
        model_obj1.attr1 = "value1"
        model_obj2 = Model()
        model_obj2.attr1 = "value1"
        self.assertEqual(model_obj1, model_obj2)

    def test_ne(self):
        # Test case for unsuccessful comparison of two model objects
        model_obj1 = Model()
        model_obj1.attr1 = "value1"
        model_obj2 = Model()
        model_obj2.attr1 = "value2"
        self.assertNotEqual(model_obj1, model_obj2)