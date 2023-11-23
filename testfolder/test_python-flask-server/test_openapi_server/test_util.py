from python-flask-server.openapi_server.util import *
import unittest
import datetime
from openapi_server import typing_utils

class TestDeserialize(unittest.TestCase):
    def test_deserialize_primitive(self):
        self.assertEqual(_deserialize_primitive(1, int), 1)
        self.assertEqual(_deserialize_primitive(1.0, float), 1.0)
        self.assertEqual(_deserialize_primitive('string', str), 'string')
        self.assertEqual(_deserialize_primitive(True, bool), True)

    def test_deserialize_object(self):
        self.assertEqual(_deserialize_object('test'), 'test')

    def test_deserialize_date(self):
        self.assertEqual(deserialize_date('2021-09-01'), datetime.date(2021, 9, 1))
        self.assertIsNone(deserialize_date(None))

    def test_deserialize_datetime(self):
        self.assertEqual(deserialize_datetime('2021-09-01T10:00:00Z'), datetime.datetime(2021, 9, 1, 10, 0, 0))
        self.assertIsNone(deserialize_datetime(None))

    def test_deserialize_model(self):
        class TestModel:
            openapi_types = {
                'str': str,
                'int': int,
                'list': list,
                'dict': dict
            }
            attribute_map = {
                'str': 'str',
                'int': 'int',
                'list': 'list',
                'dict': 'dict'
            }
            def __init__(self, str=None, int=None, list=None, dict=None):
                self.str = str
                self.int = int
                self.list = list
                self.dict = dict

        data = {
            'str': 'test',
            'int': 1,
            'list': [1, 2, 3],
            'dict': {'key': 'value'}
        }
        instance = deserialize_model(data, TestModel)
        self.assertIsInstance(instance, TestModel)
        self.assertEqual(instance.str, 'test')
        self.assertEqual(instance.int, 1)
        self.assertEqual(instance.list, [1, 2, 3])
        self.assertEqual(instance.dict, {'key': 'value'})

    def test_deserialize_list(self):
        data = [1, 2, 3]
        self.assertEqual(_deserialize_list(data, int), [1, 2, 3])

    def test_deserialize_dict(self):
        data = {'key': 'value'}
        self.assertEqual(_deserialize_dict(data, str), {'key': 'value'})