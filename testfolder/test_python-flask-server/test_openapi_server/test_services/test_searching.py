from python-flask-server.openapi_server.services.searching import *
import unittest

class TestSearching(unittest.TestCase):
    def test_equal_operator(self):
        search_params = 'name = "John"'
        Model = User
        result = searching(search_params, Model)
        self.assertEqual(result.first().name, "John")

    def test_less_than_operator(self):
        search_params = 'age < 30'
        Model = User
        result = searching(search_params, Model)
        self.assertLess(result.first().age, 30)

    def test_greater_than_operator(self):
        search_params = 'age > 25'
        Model = User
        result = searching(search_params, Model)
        self.assertGreater(result.first().age, 25)

    def test_less_than_or_equal_to_operator(self):
        search_params = 'age <= 30'
        Model = User
        result = searching(search_params, Model)
        self.assertLessEqual(result.first().age, 30)

    def test_greater_than_or_equal_to_operator(self):
        search_params = 'age >= 25'
        Model = User
        result = searching(search_params, Model)
        self.assertGreaterEqual(result.first().age, 25)

    def test_like_operator(self):
        search_params = 'email like "%@gmail.com"'
        Model = User
        result = searching(search_params, Model)
        self.assertIn('@gmail.com', result.first().email)

    def test_between_operator(self):
        search_params = 'age BETWEEN 20 AND 30'
        Model = User
        result = searching(search_params, Model)
        self.assertGreaterEqual(result.first().age, 20)
        self.assertLessEqual(result.first().age, 30)

    def test_multiple_filters(self):
        search_params = 'age > 25; name = "John"; email like "%@gmail.com"'
        Model = User
        result = searching(search_params, Model)
        self.assertGreater(result.first().age, 25)
        self.assertEqual(result.first().name, "John")
        self.assertIn('@gmail.com', result.first().email)

if __name__ == '__main__':
    unittest.main()