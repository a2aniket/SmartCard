from python-flask-server.openapi_server.services.searching import *
import unittest

class TestSearch(unittest.TestCase):
    def test_search_with_no_params(self):
        result = searching('', Model)
        self.assertEqual(result.all(), Model.query.all())

    def test_search_with_single_criteria(self):
        result = searching('name = "John"', Model)
        self.assertEqual(result.all(), Model.query.filter_by(name='John').all())

    def test_search_with_multiple_criteria(self):
        result = searching('age > 30; city like "New%"', Model)
        self.assertEqual(result.all(), Model.query.filter(Model.age > 30, Model.city.like('New%')).all())

    def test_search_with_between_operator(self):
        result = searching('id BETWEEN 5 AND 10', Model)
        self.assertEqual(result.all(), Model.query.filter(Model.id.between(5, 10)).all())

    def test_search_with_invalid_operator(self):
        with self.assertRaises(AttributeError):
            searching('name != "John"', Model)

    def test_search_with_invalid_value(self):
        with self.assertRaises(ValueError):
            searching('age > thirty', Model)

if __name__ == '__main__':
    unittest.main()