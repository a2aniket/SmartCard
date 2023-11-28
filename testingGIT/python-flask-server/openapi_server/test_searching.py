from services.searching import *
import unittest

class TestSearching(unittest.TestCase):

    def test_empty_search_params(self):
        search_params = None
        Model = None
        result = searching(search_params, Model)
        self.assertEqual(result, Model.query)

    def test_search_by_equal_operator(self):
        search_params = "name = 'John'"
        Model = User
        result = searching(search_params, Model)
        expected = Model.query.filter_by(name='John')
        self.assertEqual(result, expected)

    def test_search_by_less_than_operator(self):
        search_params = "age < 30"
        Model = User
        result = searching(search_params, Model)
        expected = Model.query.filter(User.age < 30)
        self.assertEqual(result, expected)

    def test_search_by_greater_than_operator(self):
        search_params = "age > 30"
        Model = User
        result = searching(search_params, Model)
        expected = Model.query.filter(User.age > 30)
        self.assertEqual(result, expected)

    def test_search_by_less_than_or_equal_to_operator(self):
        search_params = "age <= 30"
        Model = User
        result = searching(search_params, Model)
        expected = Model.query.filter(User.age <= 30)
        self.assertEqual(result, expected)

    def test_search_by_greater_than_or_equal_to_operator(self):
        search_params = "age >= 30"
        Model = User
        result = searching(search_params, Model)
        expected = Model.query.filter(User.age >= 30)
        self.assertEqual(result, expected)

    def test_search_by_like_operator(self):
        search_params = "name like '%John%'"
        Model = User
        result = searching(search_params, Model)
        expected = Model.query.filter(User.name.like('%John%'))
        self.assertEqual(result, expected)

    def test_search_by_between_operator(self):
        search_params = "age BETWEEN 20 AND 30"
        Model = User
        result = searching(search_params, Model)
        expected = Model.query.filter(User.age.between(20, 30))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()