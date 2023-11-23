from python-flask-server.openapi_server.services.searching import *
import unittest

class TestSearching(unittest.TestCase):
    def setUp(self):
        self.Model = Model # define the Model object
        self.search_params = "" # define empty search parameters

    def test_empty_search_params(self):
        # Test when search parameters are empty
        result = searching(self.search_params, self.Model)
        self.assertEqual(len(result.all()), len(self.Model.query.all()))

    def test_search_by_equal_operator(self):
        # Test when searching by equal operator
        self.search_params = "field = value"
        result = searching(self.search_params, self.Model)
        self.assertEqual(len(result.all()), len(self.Model.query.filter(Model.field == "value").all()))

    def test_search_by_less_than_operator(self):
        # Test when searching by less than operator
        self.search_params = "field < 5"
        result = searching(self.search_params, self.Model)
        self.assertEqual(len(result.all()), len(self.Model.query.filter(Model.field < 5).all()))

    def test_search_by_greater_than_operator(self):
        # Test when searching by greater than operator
        self.search_params = "field > 10"
        result = searching(self.search_params, self.Model)
        self.assertEqual(len(result.all()), len(self.Model.query.filter(Model.field > 10).all()))

    def test_search_by_less_than_or_equal_to_operator(self):
        # Test when searching by less than or equal to operator
        self.search_params = "field <= 3"
        result = searching(self.search_params, self.Model)
        self.assertEqual(len(result.all()), len(self.Model.query.filter(Model.field <= 3).all()))

    def test_search_by_greater_than_or_equal_to_operator(self):
        # Test when searching by greater than or equal to operator
        self.search_params = "field >= 7"
        result = searching(self.search_params, self.Model)
        self.assertEqual(len(result.all()), len(self.Model.query.filter(Model.field >= 7).all()))

    def test_search_by_like_operator(self):
        # Test when searching by like operator
        self.search_params = 'field like "%value%"'
        result = searching(self.search_params, self.Model)
        self.assertEqual(len(result.all()), len(self.Model.query.filter(Model.field.like("%value%")).all()))

    def test_search_by_between_operator(self):
        # Test when searching by between operator
        self.search_params = "field BETWEEN 5 AND 10"
        result = searching(self.search_params, self.Model)
        self.assertEqual(len(result.all()), len(self.Model.query.filter(Model.field.between(5, 10)).all()))

if __name__ == '__main__':
    unittest.main()