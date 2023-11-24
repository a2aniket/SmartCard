from python-flask-server.openapi_server.util import *
import unittest
from datetime import datetime, date
from openapi_server import typing_utils, deserialize_date, deserialize_datetime, deserialize_model, _deserialize, _deserialize_primitive, _deserialize_object, _deserialize_list, _deserialize_dict


class TestDeserialize(unittest.TestCase):
    
    def test_deserialize_none(self):
        self.assertIsNone(_deserialize(None, object))

    def test_deserialize_primitive(self):
        self.assertEqual(_deserialize_primitive('test', str), 'test')
        self.assertEqual(_deserialize_primitive(1, int), 1)
        self.assertEqual(_deserialize_primitive(1.0, float), 1.0)
        self.assertEqual(_deserialize_primitive(True, bool), True)

    def test_deserialize_object(self):
        obj = {'key': 'value'}
        self.assertEqual(_deserialize_object(obj), obj)

    def test_deserialize_date(self):
        self.assertIsNone(deserialize_date(None))
        self.assertEqual(deserialize_date('2022-01-01'), date(2022, 1, 1))

    def test_deserialize_datetime(self):
        self.assertIsNone(deserialize_datetime(None))
        self.assertEqual(deserialize_datetime('2022-01-01T12:00:00Z'), datetime(2022, 1, 1, 12, 0, 0))

    def test_deserialize_model(self):
        class TestModel:
            openapi_types = {'key': str}
            attribute_map = {'key': 'key'}
        
        data = {'key': 'value'}
        instance = deserialize_model(data, TestModel)
        self.assertEqual(instance.key, 'value')

    def test_deserialize_list(self):
        data = [1, 2, 3]
        boxed_type = int
        self.assertEqual(_deserialize_list(data, boxed_type), [1, 2, 3])

    def test_deserialize_dict(self):
        data = {'key': 'value'}
        boxed_type = str
        self.assertEqual(_deserialize_dict(data, boxed_type), {'key': 'value'})

if __name__ == '__main__':
    unittest.main()