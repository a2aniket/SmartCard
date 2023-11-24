from python-flask-server.openapi_server.typing_utils import *
import unittest
import typing

class TestIsGeneric(unittest.TestCase):
    def test_is_generic_with_generic_class(self):
        class MyGeneric(typing.Generic):
            pass
        self.assertTrue(is_generic(MyGeneric))
    
    def test_is_generic_with_non_generic_class(self):
        class MyClass:
            pass
        self.assertFalse(is_generic(MyClass))

class TestIsDict(unittest.TestCase):
    def test_is_dict_with_dict(self):
        self.assertTrue(is_dict(typing.Dict))
    
    def test_is_dict_with_non_dict(self):
        self.assertFalse(is_dict(typing.List))

class TestIsList(unittest.TestCase):
    def test_is_list_with_list(self):
        self.assertTrue(is_list(typing.List))
    
    def test_is_list_with_non_list(self):
        self.assertFalse(is_list(typing.Dict))