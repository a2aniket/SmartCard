from python-flask-server.openapi_server.typing_utils import *
import unittest
import sys
import typing

class TestIsGeneric(unittest.TestCase):
    def test_is_generic_true(self):
        self.assertTrue(is_generic(typing.List[int])) # test with List[int]
        self.assertTrue(is_generic(typing.Dict[str, int])) # test with Dict[str, int]
        self.assertTrue(is_generic(typing.Tuple[int, str])) # test with Tuple[int, str]

    def test_is_generic_false(self):
        self.assertFalse(is_generic(list)) # test with built-in list
        self.assertFalse(is_generic(dict)) # test with built-in dict

class TestIsDict(unittest.TestCase):
    def test_is_dict_true(self):
        self.assertTrue(is_dict(typing.Dict[str, int])) # test with Dict[str, int]

    def test_is_dict_false(self):
        self.assertFalse(is_dict(list)) # test with built-in list
        self.assertFalse(is_dict(dict)) # test with built-in dict
        self.assertFalse(is_dict(typing.List[int])) # test with List[int]

class TestIsList(unittest.TestCase):
    def test_is_list_true(self):
        self.assertTrue(is_list(typing.List[int])) # test with List[int]

    def test_is_list_false(self):
        self.assertFalse(is_list(dict)) # test with built-in dict
        self.assertFalse(is_list(list)) # test with built-in list
        self.assertFalse(is_list(typing.Dict[str, int])) # test with Dict[str, int]