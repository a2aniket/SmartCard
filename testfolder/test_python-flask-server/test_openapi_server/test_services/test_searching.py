from python-flask-server.openapi_server.services.searching import *
import unittest

class TestSearching(unittest.TestCase):

    def test_empty_search_params(self):
        search_params = ''
        Model = SomeModel
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.all())

    def test_equal_operator(self):
        search_params = 'name = "John"'
        Model = SomeModel
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter_by(name='John').all())

    def test_less_than_operator(self):
        search_params = 'age < 30'
        Model = SomeModel
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter(SomeModel.age < 30).all())

    def test_greater_than_operator(self):
        search_params = 'age > 30'
        Model = SomeModel
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter(SomeModel.age > 30).all())

    def test_less_than_equal_to_operator(self):
        search_params = 'age <= 30'
        Model = SomeModel
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter(SomeModel.age <= 30).all())

    def test_greater_than_equal_to_operator(self):
        search_params = 'age >= 30'
        Model = SomeModel
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter(SomeModel.age >= 30).all())

    def test_like_operator(self):
        search_params = 'name like "%John%"'
        Model = SomeModel
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter(SomeModel.name.like('%John%')).all())

    def test_between_operator(self):
        search_params = 'age BETWEEN 20 AND 30'
        Model = SomeModel
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter(SomeModel.age.between(20, 30)).all())