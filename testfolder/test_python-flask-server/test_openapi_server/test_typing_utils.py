from python-flask-server.openapi_server.typing_utils import *
import unittest
import sys
import typing

class TestIsGeneric(unittest.TestCase):
    def test_is_generic_true(self):
        self.assertTrue(is_generic(typing.List[int]))
        self.assertTrue(is_generic(typing.Dict[str, int]))

    def test_is_generic_false(self):
        self.assertFalse(is_generic(str))
        self.assertFalse(is_generic(int))

class TestIsDict(unittest.TestCase):
    def test_is_dict_true(self):
        self.assertTrue(is_dict(typing.Dict[str, int]))

    def test_is_dict_false(self):
        self.assertFalse(is_dict(str))
        self.assertFalse(is_dict(list))

class TestIsList(unittest.TestCase):
    def test_is_list_true(self):
        self.assertTrue(is_list(typing.List[int]))

    def test_is_list_false(self):
        self.assertFalse(is_list(str))
        self.assertFalse(is_list(dict))