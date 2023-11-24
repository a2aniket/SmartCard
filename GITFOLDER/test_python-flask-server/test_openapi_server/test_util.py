from python-flask-server.openapi_server.util import *
import unittest
from datetime import date, datetime
from openapi_server import typing_utils

class TestDeserialize(unittest.TestCase):
    def test_deserialize_primitive_int(self):
        self.assertEqual(_deserialize_primitive("10", int), 10)
        
    def test_deserialize_primitive_float(self):
        self.assertEqual(_deserialize_primitive("10.5", float), 10.5)
        
    def test_deserialize_primitive_str(self):
        self.assertEqual(_deserialize_primitive("test", str), "test")
        
    def test_deserialize_primitive_bool(self):
        self.assertEqual(_deserialize_primitive("True", bool), True)
        
    def test_deserialize_primitive_bytearray(self):
        self.assertEqual(_deserialize_primitive("test", bytearray), bytearray(b'test'))
        
    def test_deserialize_object(self):
        self.assertEqual(_deserialize_object("test"), "test")
        
    def test_deserialize_date(self):
        self.assertEqual(deserialize_date("2022-12-25"), date(2022, 12, 25))
        
    def test_deserialize_datetime(self):
        self.assertEqual(deserialize_datetime("2022-12-25T10:00:00Z"), datetime(2022, 12, 25, 10, 0, 0))
        
    def test_deserialize_model(self):
        class TestModel:
            openapi_types = {"test_attr": str}
            attribute_map = {"test_attr": "testAttr"}
        
        data = {"testAttr": "test_value"}
        instance = deserialize_model(data, TestModel)
        self.assertEqual(instance.test_attr, "test_value")
        
    def test_deserialize_list(self):
        data = ["10", "20", "30"]
        result = _deserialize_list(data, int)
        self.assertEqual(result, [10, 20, 30])
        
    def test_deserialize_dict(self):
        data = {"test_key": "test_value"}
        result = _deserialize_dict(data, str)
        self.assertEqual(result, {"test_key": "test_value"})