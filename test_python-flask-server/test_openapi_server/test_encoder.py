from python-flask-server.openapi_server.encoder import *
import unittest
from unittest.mock import Mock
from openapi_server.models.base_model_ import Model
from your_module import JSONEncoder

class TestJSONEncoder(unittest.TestCase):

    def test_default_with_model(self):
        """
        Test the default function with a model instance.
        """
        class TestModel(Model):
            openapi_types = {
                'id': 'int',
                'name': 'str'
            }
            attribute_map = {
                'id': 'id',
                'name': 'name'
            }

            def __init__(self, id=None, name=None):
                self._id = id
                self._name = name

            @property
            def id(self):
                return self._id

            @id.setter
            def id(self, value):
                self._id = value

            @property
            def name(self):
                return self._name

            @name.setter
            def name(self, value):
                self._name = value

        test_model = TestModel(id=1, name='test')
        result = JSONEncoder().default(test_model)
        self.assertEqual(result, {'id': 1, 'name': 'test'})

    def test_default_with_none_value(self):
        """
        Test the default function with a None value.
        """
        result = JSONEncoder().default(None)
        self.assertIsNone(result)

    def test_default_with_non_model(self):
        """
        Test the default function with a non-model instance.
        """
        result = JSONEncoder().default('test')
        self.assertEqual(result, 'test')