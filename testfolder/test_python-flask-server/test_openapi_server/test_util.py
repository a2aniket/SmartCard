from python-flask-server.openapi_server.util import *
import unittest
from datetime import date, datetime
from openapi_server.models import Model

class TestDeserialize(unittest.TestCase):

    def test_deserialize_primitive_int(self):
        result = _deserialize_primitive('10', int)
        self.assertEqual(result, 10)

    def test_deserialize_primitive_float(self):
        result = _deserialize_primitive('10.5', float)
        self.assertEqual(result, 10.5)

    def test_deserialize_primitive_str(self):
        result = _deserialize_primitive('test', str)
        self.assertEqual(result, 'test')

    def test_deserialize_primitive_bool(self):
        result = _deserialize_primitive('true', bool)
        self.assertEqual(result, True)

    def test_deserialize_primitive_bytearray(self):
        result = _deserialize_primitive('test', bytearray)
        self.assertEqual(result, bytearray(b'test'))

    def test_deserialize_object(self):
        result = _deserialize_object('test')
        self.assertEqual(result, 'test')

    def test_deserialize_date(self):
        result = deserialize_date('2022-01-01')
        self.assertEqual(result, date(2022, 1, 1))

    def test_deserialize_datetime(self):
        result = deserialize_datetime('2022-01-01T00:00:00Z')
        self.assertEqual(result, datetime(2022, 1, 1, 0, 0, 0))

    def test_deserialize_model(self):
        class TestModel(Model):
            openapi_types = {'test': 'str'}
            attribute_map = {'test': 'test'}

        data = {'test': 'test'}
        result = deserialize_model(data, TestModel)
        self.assertIsInstance(result, TestModel)
        self.assertEqual(result.test, 'test')

    def test_deserialize_list(self):
        result = _deserialize_list(['10', '20'], int)
        self.assertEqual(result, [10, 20])

    def test_deserialize_dict(self):
        data = {'test': '10'}
        result = _deserialize_dict(data, int)
        self.assertEqual(result, {'test': 10})