from python-flask-server.openapi_server.services.searching import *
import unittest

class TestSearching(unittest.TestCase):

    def test_search_params_none(self):
        search_params = None
        Model = SomeModel
        expected_query_search = Model.query
        self.assertEqual(searching(search_params, Model), expected_query_search)

    def test_search_params_empty_string(self):
        search_params = ''
        Model = SomeModel
        expected_query_search = Model.query
        self.assertEqual(searching(search_params, Model), expected_query_search)

    def test_search_params_single_criteria_equals(self):
        search_params = 'name = "John"'
        Model = SomeModel
        expected_query_search = Model.query.filter(Model.name == "John")
        self.assertEqual(searching(search_params, Model), expected_query_search)

    def test_search_params_single_criteria_less_than(self):
        search_params = 'age < 30'
        Model = SomeModel
        expected_query_search = Model.query.filter(Model.age < 30)
        self.assertEqual(searching(search_params, Model), expected_query_search)

    def test_search_params_single_criteria_greater_than(self):
        search_params = 'age > 30'
        Model = SomeModel
        expected_query_search = Model.query.filter(Model.age > 30)
        self.assertEqual(searching(search_params, Model), expected_query_search)

    def test_search_params_single_criteria_less_than_or_equal(self):
        search_params = 'age <= 30'
        Model = SomeModel
        expected_query_search = Model.query.filter(Model.age <= 30)
        self.assertEqual(searching(search_params, Model), expected_query_search)

    def test_search_params_single_criteria_greater_than_or_equal(self):
        search_params = 'age >= 30'
        Model = SomeModel
        expected_query_search = Model.query.filter(Model.age >= 30)
        self.assertEqual(searching(search_params, Model), expected_query_search)

    def test_search_params_single_criteria_like(self):
        search_params = 'name like "%John%"'
        Model = SomeModel
        expected_query_search = Model.query.filter(Model.name.like("%John%"))
        self.assertEqual(searching(search_params, Model), expected_query_search)

    def test_search_params_single_criteria_between(self):
        search_params = 'age BETWEEN 30 AND 40'
        Model = SomeModel
        expected_query_search = Model.query.filter(Model.age.between(30, 40))
        self.assertEqual(searching(search_params, Model), expected_query_search)

    def test_search_params_multiple_criteria(self):
        search_params = 'name = "John"; age > 30; email like "%@example.com%"'
        Model = SomeModel
        expected_query_search = Model.query.filter(
            Model.name == "John",
            Model.age > 30,
            Model.email.like("%@example.com%")
        )
        self.assertEqual(searching(search_params, Model), expected_query_search)