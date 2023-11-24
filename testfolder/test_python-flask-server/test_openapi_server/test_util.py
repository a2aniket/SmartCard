from python-flask-server.openapi_server.util import *
import unittest
import datetime
from openapi_server import typing_utils

class TestDeserialize(unittest.TestCase):

    def test_deserialize_primitive(self):
        self.assertEqual(_deserialize_primitive("5", int), 5)
        self.assertEqual(_deserialize_primitive("3.14", float), 3.14)
        self.assertEqual(_deserialize_primitive("hello", str), "hello")
        self.assertEqual(_deserialize_primitive(True, bool), True)
        self.assertEqual(_deserialize_primitive("utf-8", bytearray), bytearray(b'utf-8'))

    def test_deserialize_object(self):
        self.assertEqual(_deserialize_object("hello"), "hello")

    def test_deserialize_date(self):
        self.assertEqual(deserialize_date(None), None)
        self.assertEqual(deserialize_date("2022-11-25"), datetime.date(2022, 11, 25))

    def test_deserialize_datetime(self):
        self.assertEqual(deserialize_datetime(None), None)
        self.assertEqual(deserialize_datetime("2022-11-25T12:30:45Z"), datetime.datetime(2022, 11, 25, 12, 30, 45))

    def test_deserialize_list(self):
        self.assertEqual(_deserialize_list([1, 2, 3], int), [1, 2, 3])
        self.assertEqual(_deserialize_list(["a", "b", "c"], str), ["a", "b", "c"])

    def test_deserialize_dict(self):
        self.assertEqual(_deserialize_dict({"a": 1, "b": 2}, int), {"a": 1, "b": 2})
        self.assertEqual(_deserialize_dict({"x": "hello", "y": "world"}, str), {"x": "hello", "y": "world"})

    def test_deserialize(self):
        self.assertEqual(_deserialize(5, int), 5)
        self.assertEqual(_deserialize(True, bool), True)
        self.assertEqual(_deserialize("hello", str), "hello")
        self.assertEqual(_deserialize(datetime.date(2022, 11, 25), object), datetime.date(2022, 11, 25))
        self.assertEqual(_deserialize(datetime.datetime(2022, 11, 25, 12, 30, 45), object), datetime.datetime(2022, 11, 25, 12, 30, 45))
        self.assertEqual(_deserialize([1, 2, 3], typing.List[int]), [1, 2, 3])
        self.assertEqual(_deserialize({"a": 1, "b": 2}, typing.Dict[str, int]), {"a": 1, "b": 2})
        self.assertEqual(_deserialize({"x": "hello", "y": "world"}, typing.Dict[str, str]), {"x": "hello", "y": "world"})

if __name__ == '__main__':
    unittest.main()