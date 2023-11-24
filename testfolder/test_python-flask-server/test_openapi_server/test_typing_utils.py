from python-flask-server.openapi_server.typing_utils import *
import unittest
import sys
import typing

class TestIsGeneric(unittest.TestCase):
    def test_generic_class(self):
        class GenericClass(typing.Generic):
            pass
        self.assertTrue(is_generic(GenericClass))

    def test_non_generic_class(self):
        class NonGenericClass:
            pass
        self.assertFalse(is_generic(NonGenericClass))

class TestIsDict(unittest.TestCase):
    def test_dict(self):
        DictClass = typing.Dict[int, str]
        self.assertTrue(is_dict(DictClass))

    def test_non_dict(self):
        ListClass = typing.List[int]
        self.assertFalse(is_dict(ListClass))

class TestIsList(unittest.TestCase):
    def test_list(self):
        ListClass = typing.List[int]
        self.assertTrue(is_list(ListClass))

    def test_non_list(self):
        DictClass = typing.Dict[int, str]
        self.assertFalse(is_list(DictClass))