from python-flask-server.openapi_server.util import *
import datetime
import six
import typing
import unittest
from openapi_server import typing_utils

class Test_Deserialize(unittest.TestCase):
    def setUp(self):
        pass

    def test_deserialize_date(self):
        date_str = "2022-12-31"
        expected_date = datetime.date(2022, 12, 31)
        self.assertEqual(deserialize_date(date_str), expected_date)

    def test_deserialize_datetime(self):
        datetime_str = "2022-12-31T23:59:59.999999Z"
        expected_datetime = datetime.datetime(2022, 12, 31, 23, 59, 59, 999999)
        self.assertEqual(deserialize_datetime(datetime_str), expected_datetime)

    def test_deserialize_primitive_int(self):
        int_data = 123
        self.assertEqual(_deserialize_primitive(int_data, int), 123)

    def test_deserialize_primitive_float(self):
        float_data = 123.456
        self.assertEqual(_deserialize_primitive(float_data, float), 123.456)

    def test_deserialize_primitive_bool(self):
        bool_data = True
        self.assertEqual(_deserialize_primitive(bool_data, bool), True)

    def test_deserialize_primitive_str(self):
        str_data = "test"
        self.assertEqual(_deserialize_primitive(str_data, str), "test")

    def test_deserialize_primitive_bytearray(self):
        bytearray_data = bytearray(b'test')
        self.assertEqual(_deserialize_primitive(bytearray_data, bytearray), bytearray(b'test'))

    def test_deserialize_object(self):
        obj_data = {"test": "data"}
        self.assertEqual(_deserialize_object(obj_data), obj_data)

    def test_deserialize_model(self):
        data = {"attr1": "value1", "attr2": "value2"}
        klass = typing.NamedTuple("TestModel", [("attr1", str), ("attr2", str)])
        expected_instance = klass(attr1="value1", attr2="value2")
        self.assertEqual(deserialize_model(data, klass), expected_instance)

    def test_deserialize_list(self):
        data = ["value1", "value2"]
        expected_list = ["value1", "value2"]
        self.assertEqual(_deserialize_list(data, str), expected_list)

    def test_deserialize_dict(self):
        data = {"key1": "value1", "key2": "value2"}
        expected_dict = {"key1": "value1", "key2": "value2"}
        self.assertEqual(_deserialize_dict(data, str), expected_dict)

if __name__ == '__main__':
    unittest.main()