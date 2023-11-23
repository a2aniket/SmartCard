from python-flask-server.openapi_server.util import *
import unittest
from datetime import date, datetime
from openapi_server import typing_utils, _deserialize, deserialize_date, deserialize_datetime, deserialize_model


class TestDeserialize(unittest.TestCase):
    def test__deserialize_primitive_int(self):
        result = _deserialize(5, int)
        self.assertEqual(result, 5)

    def test__deserialize_primitive_float(self):
        result = _deserialize(5.5, float)
        self.assertEqual(result, 5.5)

    def test__deserialize_primitive_str(self):
        result = _deserialize("test", str)
        self.assertEqual(result, "test")

    def test__deserialize_primitive_bool_true(self):
        result = _deserialize(True, bool)
        self.assertEqual(result, True)

    def test__deserialize_primitive_bool_false(self):
        result = _deserialize(False, bool)
        self.assertEqual(result, False)

    def test__deserialize_primitive_bytearray(self):
        result = _deserialize("test".encode(), bytearray)
        self.assertEqual(result, bytearray(b'test'))

    def test__deserialize_object(self):
        result = _deserialize("test", object)
        self.assertEqual(result, "test")

    def test_deserialize_date(self):
        result = deserialize_date("2022-01-01")
        self.assertIsInstance(result, date)
        self.assertEqual(result.year, 2022)
        self.assertEqual(result.month, 1)
        self.assertEqual(result.day, 1)

    def test_deserialize_datetime(self):
        result = deserialize_datetime("2022-01-01T00:00:00.000Z")
        self.assertIsInstance(result, datetime)
        self.assertEqual(result.year, 2022)
        self.assertEqual(result.month, 1)
        self.assertEqual(result.day, 1)
        self.assertEqual(result.hour, 0)
        self.assertEqual(result.minute, 0)
        self.assertEqual(result.second, 0)
        self.assertEqual(result.microsecond, 0)

    def test_deserialize_model(self):
        class TestModel:
            def __init__(self):
                self.openapi_types = {"attr": str}
                self.attribute_map = {"attr": "attr"}

        test_data = {"attr": "test"}
        result = deserialize_model(test_data, TestModel)
        self.assertIsInstance(result, TestModel)
        self.assertEqual(result.attr, "test")

    def test__deserialize_list(self):
        result = _deserialize([1, 2, 3], typing.List[int])
        self.assertIsInstance(result, list)
        self.assertEqual(result, [1, 2, 3])

    def test__deserialize_dict(self):
        result = _deserialize({"key": "value"}, typing.Dict[str, str])
        self.assertIsInstance(result, dict)
        self.assertEqual(result, {"key": "value"})