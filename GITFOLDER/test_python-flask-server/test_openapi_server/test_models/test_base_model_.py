from python-flask-server.openapi_server.models.base_model_ import *
import unittest
from openapi_server.models import Model

class TestModel(unittest.TestCase):
    def test_from_dict(self):
        # Test that the from_dict method returns an instance of the Model class
        dikt = {}
        model = Model.from_dict(dikt)
        self.assertIsInstance(model, Model)

    def test_to_dict(self):
        # Test that the to_dict method returns a dictionary
        model = Model()
        dikt = model.to_dict()
        self.assertIsInstance(dikt, dict)

    def test_to_str(self):
        # Test that the to_str method returns a string
        model = Model()
        string = model.to_str()
        self.assertIsInstance(string, str)

    def test_repr(self):
        # Test that the __repr__ method returns a string
        model = Model()
        string = model.__repr__()
        self.assertIsInstance(string, str)

    def test_eq(self):
        # Test that the __eq__ method returns True when objects are equal and False when they are not
        model1 = Model()
        model2 = Model()
        self.assertEqual(model1, model2)

        model3 = Model()
        model3.openapi_types = {'attr': str}
        self.assertNotEqual(model1, model3)

    def test_ne(self):
        # Test that the __ne__ method returns True when objects are not equal and False when they are
        model1 = Model()
        model2 = Model()
        self.assertFalse(model1.__ne__(model2))

        model3 = Model()
        model3.openapi_types = {'attr': str}
        self.assertTrue(model1.__ne__(model3))