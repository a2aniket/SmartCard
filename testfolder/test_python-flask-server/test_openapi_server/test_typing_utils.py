from python-flask-server.openapi_server.typing_utils import *
import unittest
import sys
import typing

class TestIsGeneric(unittest.TestCase):
    def test_is_generic(self):
        self.assertTrue(is_generic(typing.List[int]))
        self.assertTrue(is_generic(typing.Dict[str, int]))
        self.assertFalse(is_generic(int))
        self.assertFalse(is_generic(str))

class TestIsDict(unittest.TestCase):
    def test_is_dict(self):
        self.assertTrue(is_dict(typing.Dict[str, int]))
        self.assertFalse(is_dict(typing.List[int]))
        self.assertFalse(is_dict(int))
        self.assertFalse(is_dict(str))

class TestIsList(unittest.TestCase):
    def test_is_list(self):
        self.assertTrue(is_list(typing.List[int]))
        self.assertFalse(is_list(typing.Dict[str, int]))
        self.assertFalse(is_list(int))
        self.assertFalse(is_list(str))