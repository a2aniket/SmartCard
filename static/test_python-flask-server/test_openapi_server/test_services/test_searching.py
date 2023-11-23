from python-flask-server.openapi_server.services.searching import *
import unittest

class TestSearching(unittest.TestCase):
    def test_searching_with_no_params(self):
        result = searching(None, Model)
        self.assertEqual(result.all(), Model.query.all())

    def test_searching_with_single_field_equal(self):
        search_params = "name = 'John'"
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter_by(name='John').all())

    def test_searching_with_single_field_less_than(self):
        search_params = "age < 30"
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter(Model.age < 30).all())

    def test_searching_with_single_field_greater_than(self):
        search_params = "age > 30"
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter(Model.age > 30).all())

    def test_searching_with_single_field_less_than_or_equal_to(self):
        search_params = "age <= 30"
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter(Model.age <= 30).all())

    def test_searching_with_single_field_greater_than_or_equal_to(self):
        search_params = "age >= 30"
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter(Model.age >= 30).all())

    def test_searching_with_single_field_like(self):
        search_params = 'name like "%ohn%"'
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter(Model.name.like('%ohn%')).all())

    def test_searching_with_single_field_between(self):
        search_params = "id BETWEEN 2 AND 7"
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter(Model.id.between(2, 7)).all())

    def test_searching_with_multiple_filters(self):
        search_params = 'name = "John"; age > 30; email like "%@gmail.com"'
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter_by(name='John').filter(Model.age > 30).filter(Model.email.like('%@gmail.com')).all())

if __name__ == '__main__':
    unittest.main()