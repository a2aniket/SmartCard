from python-flask-server.openapi_server.services.searching import *
import unittest

class TestSearching(unittest.TestCase):

    def test_searching_with_empty_params(self):
        search_params = ''
        Model = None
        result = searching(search_params, Model)
        self.assertEqual(result.count(), Model.query.count())

    def test_searching_with_one_criterion(self):
        search_params = 'name = "John"'
        Model = MockModel(name="John")
        result = searching(search_params, Model)
        self.assertEqual(result.count(), 1)

    def test_searching_with_multiple_criteria(self):
        search_params = 'name = "John";age > 18;email like "%@gmail.com"'
        Model = MockModel(name="John", age=20, email="john@gmail.com")
        result = searching(search_params, Model)
        self.assertEqual(result.count(), 1)

    def test_searching_with_incorrect_operator(self):
        search_params = 'name == "John"'
        Model = MockModel(name="John")
        with self.assertRaises(ValueError):
            searching(search_params, Model)

    def test_searching_with_between_operator(self):
        search_params = 'age BETWEEN 18 AND 30'
        Model = MockModel(age=20)
        result = searching(search_params, Model)
        self.assertEqual(result.count(), 1)

class MockModel():
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def __getattr__(self, key):
        return self.attributes[key]

    def query(self):
        return self

if __name__ == '__main__':
    unittest.main()