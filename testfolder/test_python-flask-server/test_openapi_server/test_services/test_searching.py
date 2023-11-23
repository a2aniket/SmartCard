from python-flask-server.openapi_server.services.searching import *
import unittest

class TestSearching(unittest.TestCase):
    def test_no_search_params(self):
        from models import Model # assuming Model is defined in another file
        result = searching(None, Model)
        self.assertEqual(result, Model.query)

    def test_single_equal_operator(self):
        from models import Model
        result = searching("name = 'John'", Model)
        query_filters = [getattr(Model, 'name') == 'John']
        expected_query = Model.query.filter(*query_filters)
        self.assertEqual(result, expected_query)

    def test_single_less_than_operator(self):
        from models import Model
        result = searching("age < 18", Model)
        query_filters = [getattr(Model, 'age') < 18]
        expected_query = Model.query.filter(*query_filters)
        self.assertEqual(result, expected_query)

    def test_single_greater_than_operator(self):
        from models import Model
        result = searching("salary > 50000", Model)
        query_filters = [getattr(Model, 'salary') > 50000]
        expected_query = Model.query.filter(*query_filters)
        self.assertEqual(result, expected_query)

    def test_single_less_than_equal_to_operator(self):
        from models import Model
        result = searching("age <= 18", Model)
        query_filters = [getattr(Model, 'age') <= 18]
        expected_query = Model.query.filter(*query_filters)
        self.assertEqual(result, expected_query)

    def test_single_greater_than_equal_to_operator(self):
        from models import Model
        result = searching("salary >= 50000", Model)
        query_filters = [getattr(Model, 'salary') >= 50000]
        expected_query = Model.query.filter(*query_filters)
        self.assertEqual(result, expected_query)

    def test_single_like_operator(self):
        from models import Model
        result = searching('name like "%ohn%"', Model)
        query_filters = [getattr(Model, 'name').like('%ohn%')]
        expected_query = Model.query.filter(*query_filters)
        self.assertEqual(result, expected_query)

    def test_single_between_operator(self):
        from models import Model
        result = searching('age BETWEEN 18 AND 25', Model)
        query_filters = [getattr(Model, 'age').between(18, 25)]
        expected_query = Model.query.filter(*query_filters)
        self.assertEqual(result, expected_query)

    def test_multiple_criteria(self):
        from models import Model
        result = searching('name = "John"; salary > 50000', Model)
        query_filters = [
            getattr(Model, 'name') == 'John',
            getattr(Model, 'salary') > 50000,
        ]
        expected_query = Model.query.filter(*query_filters)
        self.assertEqual(result, expected_query)

if __name__ == '__main__':
    unittest.main()