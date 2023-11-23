from python-flask-server.openapi_server.services.searching import *
import unittest

class TestSearching(unittest.TestCase):
    def test_no_search_params(self):
        result = searching(None, Model)
        self.assertEqual(result.all(), Model.query.all())

    def test_equal_operator(self):
        result = searching('name = "John"', Model)
        self.assertEqual(result.all(), Model.query.filter(Model.name == "John").all())

    def test_less_than_operator(self):
        result = searching('age < 30', Model)
        self.assertEqual(result.all(), Model.query.filter(Model.age < 30).all())

    def test_greater_than_operator(self):
        result = searching('age > 30', Model)
        self.assertEqual(result.all(), Model.query.filter(Model.age > 30).all())

    def test_less_than_equal_to_operator(self):
        result = searching('age <= 30', Model)
        self.assertEqual(result.all(), Model.query.filter(Model.age <= 30).all())

    def test_greater_than_equal_to_operator(self):
        result = searching('age >= 30', Model)
        self.assertEqual(result.all(), Model.query.filter(Model.age >= 30).all())

    def test_like_operator(self):
        result = searching('name like "%John%"', Model)
        self.assertEqual(result.all(), Model.query.filter(Model.name.like("%John%")).all())

    def test_between_operator(self):
        result = searching('age BETWEEN 20 AND 30', Model)
        self.assertEqual(result.all(), Model.query.filter(Model.age.between(20, 30)).all())

if __name__ == '__main__':
    unittest.main()