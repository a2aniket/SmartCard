from python-flask-server.openapi_server.typing_utils import *
import unittest
import sys
import typing

class TestIsGeneric(unittest.TestCase):
    def test_is_generic_with_generic_class(self):
        self.assertTrue(is_generic(typing.List[int]))

    def test_is_generic_with_non_generic_class(self):
        self.assertFalse(is_generic(int))

class TestIsDict(unittest.TestCase):
    def test_is_dict_with_dict(self):
        self.assertTrue(is_dict(typing.Dict[int, str]))

    def test_is_dict_with_non_dict(self):
        self.assertFalse(is_dict(list))

class TestIsList(unittest.TestCase):
    def test_is_list_with_list(self):
        self.assertTrue(is_list(typing.List[int]))

    def test_is_list_with_non_list(self):
        self.assertFalse(is_list(dict))