from python-flask-server.openapi_server.models.base_model_ import *
import unittest
from openapi_server import util

class TestModel(unittest.TestCase):
    def test_from_dict(self):
        # Test for correct conversion of dict to model
        dikt = {'attribute1': 'value1', 'attribute2': 'value2', 'attribute3': {'subattribute1': 'subvalue1'}}
        model_instance = util.deserialize_model(dikt, Model)
        self.assertIsInstance(model_instance, Model)
        self.assertEqual(model_instance.attribute1, 'value1')
        self.assertEqual(model_instance.attribute2, 'value2')
        self.assertIsInstance(model_instance.attribute3, dict)
        self.assertEqual(model_instance.attribute3['subattribute1'], 'subvalue1')

    def test_to_dict(self):
        # Test for correct conversion of model to dict
        model_instance = Model()
        model_instance.attribute1 = 'value1'
        model_instance.attribute2 = 'value2'
        model_instance.attribute3 = {'subattribute1': 'subvalue1'}
        dikt = model_instance.to_dict()
        self.assertIsInstance(dikt, dict)
        self.assertEqual(dikt['attribute1'], 'value1')
        self.assertEqual(dikt['attribute2'], 'value2')
        self.assertIsInstance(dikt['attribute3'], dict)
        self.assertEqual(dikt['attribute3']['subattribute1'], 'subvalue1')

    def test_to_str(self):
        # Test for correct string representation of model
        model_instance = Model()
        model_instance.attribute1 = 'value1'
        model_instance.attribute2 = 'value2'
        model_instance.attribute3 = {'subattribute1': 'subvalue1'}
        string = model_instance.to_str()
        self.assertIsInstance(string, str)
        self.assertIn('attribute1', string)
        self.assertIn('value1', string)
        self.assertIn('attribute2', string)
        self.assertIn('value2', string)
        self.assertIn('attribute3', string)
        self.assertIn('subattribute1', string)
        self.assertIn('subvalue1', string)

    def test___eq__(self):
        # Test for correct equality comparison of models
        model_instance1 = Model()
        model_instance1.attribute1 = 'value1'
        model_instance1.attribute2 = 'value2'
        model_instance1.attribute3 = {'subattribute1': 'subvalue1'}
        model_instance2 = Model()
        model_instance2.attribute1 = 'value1'
        model_instance2.attribute2 = 'value2'
        model_instance2.attribute3 = {'subattribute1': 'subvalue1'}
        self.assertEqual(model_instance1, model_instance2)

    def test___ne__(self):
        # Test for correct non-equality comparison of models
        model_instance1 = Model()
        model_instance1.attribute1 = 'value1'
        model_instance1.attribute2 = 'value2'
        model_instance1.attribute3 = {'subattribute1': 'subvalue1'}
        model_instance2 = Model()
        model_instance2.attribute1 = 'value1'
        model_instance2.attribute2 = 'value2'
        model_instance2.attribute3 = {'subattribute1': 'subvalue2'}
        self.assertNotEqual(model_instance1, model_instance2)