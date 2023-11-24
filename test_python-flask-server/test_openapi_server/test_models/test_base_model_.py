from python-flask-server.openapi_server.models.base_model_ import *
import unittest

class TestModel(unittest.TestCase):

    def test_from_dict(self):
        # Test 1: Test with empty dictionary
        dikt = {}
        model = Model.from_dict(dikt)
        self.assertEqual(model.__dict__, {})

        # Test 2: Test with dictionary having one attribute
        dikt = {"attribute1": "value1"}
        model = Model.from_dict(dikt)
        self.assertEqual(model.__dict__, {"attribute1": "value1"})

        # Test 3: Test with dictionary having multiple attributes
        dikt = {"attribute1": "value1", "attribute2": 2}
        model = Model.from_dict(dikt)
        self.assertEqual(model.__dict__, {"attribute1": "value1", "attribute2": 2})

    def test_to_dict(self):
        # Test 1: Test with empty model object
        model = Model()
        dikt = model.to_dict()
        self.assertEqual(dikt, {})

        # Test 2: Test with model object having one attribute
        model.attribute1 = "value1"
        dikt = model.to_dict()
        self.assertEqual(dikt, {"attribute1": "value1"})

        # Test 3: Test with model object having multiple attributes
        model.attribute2 = 2
        dikt = model.to_dict()
        self.assertEqual(dikt, {"attribute1": "value1", "attribute2": 2})

    def test_to_str(self):
        # Test 1: Test with empty model object
        model = Model()
        str_model = model.to_str()
        self.assertEqual(str_model, "{}")

        # Test 2: Test with model object having one attribute
        model.attribute1 = "value1"
        str_model = model.to_str()
        self.assertEqual(str_model, "{'attribute1': 'value1'}")

        # Test 3: Test with model object having multiple attributes
        model.attribute2 = 2
        str_model = model.to_str()
        self.assertEqual(str_model, "{'attribute1': 'value1', 'attribute2': 2}")

    def test_eq(self):
        # Test 1: Test with empty model objects
        model1 = Model()
        model2 = Model()
        self.assertEqual(model1, model2)

        # Test 2: Test with model objects having one attribute
        model1.attribute1 = "value1"
        model2.attribute1 = "value1"
        self.assertEqual(model1, model2)

        # Test 3: Test with model objects having multiple attributes
        model1.attribute2 = 2
        model2.attribute2 = 2
        self.assertEqual(model1, model2)

    def test_ne(self):
        # Test 1: Test with empty model objects
        model1 = Model()
        model2 = Model()
        self.assertNotEqual(model1, model2)

        # Test 2: Test with model objects having one attribute
        model1.attribute1 = "value1"
        model2.attribute1 = "value2"
        self.assertNotEqual(model1, model2)

        # Test 3: Test with model objects having multiple attributes
        model1.attribute2 = 2
        model2.attribute2 = 3
        self.assertNotEqual(model1, model2)

if __name__ == '__main__':
    unittest.main()