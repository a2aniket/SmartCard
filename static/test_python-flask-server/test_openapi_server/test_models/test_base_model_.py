from python-flask-server.openapi_server.models.base_model_ import *
import unittest
from openapi_server.models import Model

class TestModel(unittest.TestCase):
    def test_from_dict(self):
        """Test if from_dict method returns model object"""
        # Test with empty dictionary
        dikt = {}
        model = Model.from_dict(dikt)
        self.assertIsInstance(model, Model)

        # Test with non-empty dictionary
        dikt = {'name': 'John', 'age': 25}
        model = Model.from_dict(dikt)
        self.assertIsInstance(model, Model)

    def test_to_dict(self):
        """Test if to_dict method returns dictionary"""
        # Test with empty model object
        model = Model()
        dikt = model.to_dict()
        self.assertIsInstance(dikt, dict)

        # Test with non-empty model object
        model.name = 'John'
        model.age = 25
        dikt = model.to_dict()
        self.assertIsInstance(dikt, dict)

    def test_to_str(self):
        """Test if to_str method returns string"""
        # Test with empty model object
        model = Model()
        string = model.to_str()
        self.assertIsInstance(string, str)

        # Test with non-empty model object
        model.name = 'John'
        model.age = 25
        string = model.to_str()
        self.assertIsInstance(string, str)

    def test_eq(self):
        """Test if __eq__ method returns correct value"""
        # Test with two empty model objects
        model1 = Model()
        model2 = Model()
        self.assertEqual(model1, model2)

        # Test with two non-empty model objects
        model1.name = 'John'
        model1.age = 25
        model2.name = 'John'
        model2.age = 25
        self.assertEqual(model1, model2)

    def test_ne(self):
        """Test if __ne__ method returns correct value"""
        # Test with two empty model objects
        model1 = Model()
        model2 = Model()
        self.assertFalse(model1 != model2)

        # Test with two non-empty model objects
        model1.name = 'John'
        model1.age = 25
        model2.name = 'John'
        model2.age = 25
        self.assertFalse(model1 != model2)

if __name__ == '__main__':
    unittest.main()