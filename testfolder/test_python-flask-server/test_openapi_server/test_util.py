from python-flask-server.openapi_server.util import *
import unittest
from datetime import datetime, date
from openapi_server import typing_utils, _deserialize, deserialize_date, deserialize_datetime, deserialize_model

class TestDeserialize(unittest.TestCase):

    def test_deserialize_primitive(self):
        self.assertEqual(_deserialize_primitive('100', int), 100)
        self.assertEqual(_deserialize_primitive('100.0', float), 100.0)
        self.assertEqual(_deserialize_primitive('True', bool), True)
        self.assertEqual(_deserialize_primitive('test', str), 'test')
        self.assertEqual(_deserialize_primitive(b'123', bytearray), bytearray(b'123'))

    def test_deserialize_object(self):
        obj = object()
        self.assertIs(_deserialize_object(obj), obj)

    def test_deserialize_date(self):
        self.assertEqual(deserialize_date('2022-12-31'), date(2022, 12, 31))
        self.assertEqual(deserialize_date(None), None)

    def test_deserialize_datetime(self):
        self.assertEqual(deserialize_datetime('2022-12-31T12:30:45.123456Z'), datetime(2022, 12, 31, 12, 30, 45, 123456))
        self.assertEqual(deserialize_datetime(None), None)

    def test_deserialize_list(self):
        data = ['1', '2', '3']
        boxed_type = int
        result = _deserialize_list(data, boxed_type)
        self.assertListEqual(result, [1, 2, 3])

    def test_deserialize_dict(self):
        data = {'a': '1', 'b': '2'}
        boxed_type = int
        result = _deserialize_dict(data, boxed_type)
        self.assertDictEqual(result, {'a': 1, 'b': 2})

    def test_deserialize_model(self):
        class TestModel:
            openapi_types = {
                'a': str, 'b': int
            }
            attribute_map = {
                'a': 'A', 'b': 'B'
            }

        data = {'A': 'test', 'B': '100'}
        result = deserialize_model(data, TestModel)
        self.assertIsInstance(result, TestModel)
        self.assertEqual(result.a, 'test')
        self.assertEqual(result.b, 100)

    def test_deserialize(self):
        data = {'a': '1', 'b': ['2', '3']}
        klass = typing.List[int]
        result = _deserialize(data, klass)
        self.assertListEqual(result, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()