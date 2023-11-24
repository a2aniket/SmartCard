from python-flask-server.openapi_server.services.searching import *
import unittest

class TestSearch(unittest.TestCase):
    def test_searching_with_empty_params(self):
        search_params = ""
        Model = None
        result = searching(search_params, Model)
        self.assertEqual(result, Model.query)

    def test_searching_with_single_criterion(self):
        search_params = "name = 'John'"
        Model = MyModel
        result = searching(search_params, Model)
        expected_query = Model.query.filter(Model.name == 'John')
        self.assertEqual(result, expected_query)

    def test_searching_with_multiple_criteria(self):
        search_params = "name = 'John'; age > 30; email like '%@example.com'"
        Model = MyModel
        result = searching(search_params, Model)
        expected_query = Model.query.filter(Model.name == 'John',
                                             Model.age > 30,
                                             Model.email.like('%@example.com'))
        self.assertEqual(result, expected_query)

    def test_searching_with_less_than_operator(self):
        search_params = "age < 30"
        Model = MyModel
        result = searching(search_params, Model)
        expected_query = Model.query.filter(Model.age < 30)
        self.assertEqual(result, expected_query)

    def test_searching_with_greater_than_operator(self):
        search_params = "age > 30"
        Model = MyModel
        result = searching(search_params, Model)
        expected_query = Model.query.filter(Model.age > 30)
        self.assertEqual(result, expected_query)

    def test_searching_with_less_than_or_equal_to_operator(self):
        search_params = "age <= 30"
        Model = MyModel
        result = searching(search_params, Model)
        expected_query = Model.query.filter(Model.age <= 30)
        self.assertEqual(result, expected_query)

    def test_searching_with_greater_than_or_equal_to_operator(self):
        search_params = "age >= 30"
        Model = MyModel
        result = searching(search_params, Model)
        expected_query = Model.query.filter(Model.age >= 30)
        self.assertEqual(result, expected_query)

    def test_searching_with_like_operator(self):
        search_params = "name like '%ohn'"
        Model = MyModel
        result = searching(search_params, Model)
        expected_query = Model.query.filter(Model.name.like('%ohn'))
        self.assertEqual(result, expected_query)

    def test_searching_with_between_operator(self):
        search_params = "age BETWEEN 20 AND 30"
        Model = MyModel
        result = searching(search_params, Model)
        expected_query = Model.query.filter(Model.age.between(20, 30))
        self.assertEqual(result, expected_query)

if __name__ == '__main__':
    unittest.main()