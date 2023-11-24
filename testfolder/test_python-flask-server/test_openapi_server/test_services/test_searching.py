from python-flask-server.openapi_server.services.searching import *
import unittest

class TestSearching(unittest.TestCase):

    def test_search_with_one_criteria(self):
        search_params = "name = 'John'"
        expected_result = Model.query.filter(Model.name == 'John')
        self.assertEqual(searching(search_params, Model).all(), expected_result.all())

    def test_search_with_multiple_criteria(self):
        search_params = "name = 'John'; age > 25; job_title like '%Engineer%'"
        expected_result = Model.query.filter(Model.name == 'John', Model.age > 25, Model.job_title.like('%Engineer%'))
        self.assertEqual(searching(search_params, Model).all(), expected_result.all())

    def test_search_with_less_than_operator(self):
        search_params = "age < 30"
        expected_result = Model.query.filter(Model.age < 30)
        self.assertEqual(searching(search_params, Model).all(), expected_result.all())

    def test_search_with_greater_than_operator(self):
        search_params = "age > 30"
        expected_result = Model.query.filter(Model.age > 30)
        self.assertEqual(searching(search_params, Model).all(), expected_result.all())

    def test_search_with_less_than_or_equal_to_operator(self):
        search_params = "age <= 30"
        expected_result = Model.query.filter(Model.age <= 30)
        self.assertEqual(searching(search_params, Model).all(), expected_result.all())

    def test_search_with_greater_than_or_equal_to_operator(self):
        search_params = "age >= 30"
        expected_result = Model.query.filter(Model.age >= 30)
        self.assertEqual(searching(search_params, Model).all(), expected_result.all())

    def test_search_with_like_operator(self):
        search_params = "name like '%John%'"
        expected_result = Model.query.filter(Model.name.like('%John%'))
        self.assertEqual(searching(search_params, Model).all(), expected_result.all())

    def test_search_with_between_operator(self):
        search_params = "age BETWEEN 25 AND 30"
        expected_result = Model.query.filter(Model.age.between(25, 30))
        self.assertEqual(searching(search_params, Model).all(), expected_result.all())

    def test_search_without_search_params(self):
        search_params = ""
        expected_result = Model.query
        self.assertEqual(searching(search_params, Model).all(), expected_result.all())

if __name__ == '__main__':
    unittest.main()