from python-flask-server.openapi_server.services.searching import *
import unittest

class TestSearching(unittest.TestCase):
    def test_search_criteria_equal(self):
        search_params = 'name = "John"'
        query_search = searching(search_params, Model)
        self.assertEqual(len(query_search.all()), 1)
    
    def test_search_criteria_less_than(self):
        search_params = 'age < 30'
        query_search = searching(search_params, Model)
        self.assertLess(query_search.first().age, 30)
    
    def test_search_criteria_greater_than(self):
        search_params = 'age > 30'
        query_search = searching(search_params, Model)
        self.assertGreater(query_search.first().age, 30)
    
    def test_search_criteria_less_than_or_equal(self):
        search_params = 'age <= 30'
        query_search = searching(search_params, Model)
        self.assertLessEqual(query_search.first().age, 30)
    
    def test_search_criteria_greater_than_or_equal(self):
        search_params = 'age >= 30'
        query_search = searching(search_params, Model)
        self.assertGreaterEqual(query_search.first().age, 30)
    
    def test_search_criteria_like(self):
        search_params = 'name like "%John%"'
        query_search = searching(search_params, Model)
        self.assertTrue('John' in query_search.first().name)
    
    def test_search_criteria_between(self):
        search_params = 'age BETWEEN 20 AND 30'
        query_search = searching(search_params, Model)
        self.assertGreaterEqual(query_search.first().age, 20)
        self.assertLessEqual(query_search.first().age, 30)