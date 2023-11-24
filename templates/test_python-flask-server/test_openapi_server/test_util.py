from python-flask-server.openapi_server.util import *
import unittest
from datetime import date, datetime
from openapi_server.models import MyModel

class TestDeserialization(unittest.TestCase):
    
    def test_deserialize_primitive(self):
        self.assertEqual(_deserialize_primitive('123', int), 123)
        self.assertEqual(_deserialize_primitive('123.0', float), 123.0)
        self.assertEqual(_deserialize_primitive('true', bool), True)
        self.assertEqual(_deserialize_primitive('hello', str), 'hello')
    
    def test_deserialize_date(self):
        self.assertEqual(deserialize_date('2022-12-31'), date(2022, 12, 31))
    
    def test_deserialize_datetime(self):
        self.assertEqual(deserialize_datetime('2022-12-31T23:59:59Z'), datetime(2022, 12, 31, 23, 59, 59))
    
    def test_deserialize_model(self):
        data = {
            'id': 1,
            'name': 'John',
            'age': '25',
            'birthdate': '2000-01-01',
            'created_at': '2022-01-01T01:01:01Z',
        }
        instance = deserialize_model(data, MyModel)
        self.assertIsInstance(instance, MyModel)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.name, 'John')
        self.assertEqual(instance.age, 25)
        self.assertEqual(instance.birthdate, date(2000, 1, 1))
        self.assertEqual(instance.created_at, datetime(2022, 1, 1, 1, 1, 1))
    
    def test_deserialize_list(self):
        data = ['123', '456', '789']
        boxed_type = int
        result = _deserialize_list(data, boxed_type)
        self.assertEqual(result, [123, 456, 789])
    
    def test_deserialize_dict(self):
        data = {
            'name': 'John',
            'age': '25',
            'birthdate': '2000-01-01',
        }
        boxed_type = str
        result = _deserialize_dict(data, boxed_type)
        self.assertEqual(result, {
            'name': 'John',
            'age': '25',
            'birthdate': '2000-01-01',
        })