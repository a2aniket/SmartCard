import unittest

class TestSearching(unittest.TestCase):

    def test_search_by_equal_operator(self):
        """
        Test searching with equal operator
        """
        search_params = "name = 'John'"
        Model = MyModel
        result = searching(search_params, Model)
        expected_result = Model.query.filter(Model.name == 'John')
        self.assertEqual(result.statement, expected_result.statement)

    def test_search_by_less_than_operator(self):
        """
        Test searching with less than operator
        """
        search_params = "age < 30"
        Model = MyModel
        result = searching(search_params, Model)
        expected_result = Model.query.filter(Model.age < 30)
        self.assertEqual(result.statement, expected_result.statement)

    def test_search_by_greater_than_operator(self):
        """
        Test searching with greater than operator
        """
        search_params = "age > 30"
        Model = MyModel
        result = searching(search_params, Model)
        expected_result = Model.query.filter(Model.age > 30)
        self.assertEqual(result.statement, expected_result.statement)

    def test_search_by_less_than_equal_to_operator(self):
        """
        Test searching with less than equal to operator
        """
        search_params = "age <= 30"
        Model = MyModel
        result = searching(search_params, Model)
        expected_result = Model.query.filter(Model.age <= 30)
        self.assertEqual(result.statement, expected_result.statement)

    def test_search_by_greater_than_equal_to_operator(self):
        """
        Test searching with greater than equal to operator
        """
        search_params = "age >= 30"
        Model = MyModel
        result = searching(search_params, Model)
        expected_result = Model.query.filter(Model.age >= 30)
        self.assertEqual(result.statement, expected_result.statement)

    def test_search_by_like_operator(self):
        """
        Test searching with like operator
        """
        search_params = "email like '%@gmail.com'"
        Model = MyModel
        result = searching(search_params, Model)
        expected_result = Model.query.filter(Model.email.like('%@gmail.com'))
        self.assertEqual(result.statement, expected_result.statement)

    def test_search_by_between_operator(self):
        """
        Test searching with between operator
        """
        search_params = "age BETWEEN 20 AND 30"
        Model = MyModel
        result = searching(search_params, Model)
        expected_result = Model.query.filter(Model.age.between(20, 30))
        self.assertEqual(result.statement, expected_result.statement)

if __name__ == '__main__':
    unittest.main()