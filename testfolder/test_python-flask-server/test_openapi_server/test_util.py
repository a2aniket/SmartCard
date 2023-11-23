from python-flask-server.openapi_server.util import *
import unittest
import datetime
from openapi_server import typing_utils

class TestDeserialize(unittest.TestCase):
    
    def test_deserialize_primitive(self):
        # Test deserialization of int
        self.assertEqual(_deserialize_primitive('1', int), 1)
        self.assertEqual(_deserialize_primitive(1, int), 1)
        # Test deserialization of long
        self.assertEqual(_deserialize_primitive('1000000000000', int), 1000000000000)
        # Test deserialization of float
        self.assertEqual(_deserialize_primitive('1.5', float), 1.5)
        self.assertEqual(_deserialize_primitive(1.5, float), 1.5)
        # Test deserialization of str
        self.assertEqual(_deserialize_primitive('test', str), 'test')
        # Test deserialization of bool
        self.assertEqual(_deserialize_primitive('true', bool), True)
        self.assertEqual(_deserialize_primitive(True, bool), True)
    
    def test_deserialize_object(self):
        # Test deserialization of object
        self.assertEqual(_deserialize_object('test'), 'test')
        self.assertEqual(_deserialize_object(1), 1)
        
    def test_deserialize_date(self):
        # Test deserialization of date
        self.assertEqual(deserialize_date('2021-01-01'), datetime.date(2021, 1, 1))
        self.assertEqual(deserialize_date(None), None)
        
    def test_deserialize_datetime(self):
        # Test deserialization of datetime
        self.assertEqual(deserialize_datetime('2021-01-01T01:01:01'), datetime.datetime(2021, 1, 1, 1, 1, 1))
        self.assertEqual(deserialize_datetime(None), None)
        
    def test_deserialize_list(self):
        # Test deserialization of list
        self.assertEqual(_deserialize_list(['1', '2', '3'], int), [1, 2, 3])
        self.assertEqual(_deserialize_list([], int), [])
        
    def test_deserialize_dict(self):
        # Test deserialization of dict
        self.assertEqual(_deserialize_dict({'a': '1', 'b': '2'}, int), {'a': 1, 'b': 2})
        self.assertEqual(_deserialize_dict({}, int), {})
        
    def test_deserialize_model(self):
        # Test deserialization of model
        class TestModel:
            openapi_types = {'a': int, 'b': str}
            attribute_map = {'a': 'a', 'b': 'b'}
        data = {'a': '1', 'b': 'test'}
        instance = deserialize_model(data, TestModel)
        self.assertEqual(instance.a, 1)
        self.assertEqual(instance.b, 'test')
        
if __name__ == '__main__':
    unittest.main()