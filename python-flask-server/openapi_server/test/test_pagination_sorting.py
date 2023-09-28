import unittest
from flask import Flask
from openapi_server.models import Model
from openapi_server.routes import pagination_sorting

class TestPaginationSorting(unittest.TestCase):
    """
    This class contains the unit test cases for the pagination_sorting function.
    """

    def setUp(self):
        """
        This function is called before each test case.
        It initializes a Flask app and creates a test client.
        """
        self.app = Flask(__name__)
        self.client = self.app.test_client()
        self.model = Model()

    def test_pagination_sorting_default(self):
        """
        Test case to check if default values are returned when no query parameters are provided.
        """
        with self.app.test_request_context():
            result = pagination_sorting(self.model)
            self.assertEqual(result, self.model.query.order_by(self.model.id).paginate(page=1, per_page=10).items)

    def test_pagination_sorting_page_number(self):
        """
        Test case to check if the correct page number is returned.
        """
        with self.app.test_request_context(query_string='pageNumber=2'):
            result = pagination_sorting(self.model)
            self.assertEqual(result, self.model.query.order_by(self.model.id).paginate(page=2, per_page=10).items)

    def test_pagination_sorting_page_size(self):
        """
        Test case to check if the correct page size is returned.
        """
        with self.app.test_request_context(query_string='pageSize=25'):
            result = pagination_sorting(self.model)
            self.assertEqual(result, self.model.query.order_by(self.model.id).paginate(page=1, per_page=25).items)

    def test_pagination_sorting_sort_by(self):
        """
        Test case to check if the correct sorting column is returned.
        """
        with self.app.test_request_context(query_string='sortBy=name'):
            result = pagination_sorting(self.model)
            self.assertEqual(result, self.model.query.order_by(self.model.name).paginate(page=1, per_page=10).items)

    def test_pagination_sorting_sort_dir_asc(self):
        """
        Test case to check if the correct sorting direction is returned when 'asc' is provided.
        """
        with self.app.test_request_context(query_string='sortDir=asc'):
            result = pagination_sorting(self.model)
            self.assertEqual(result, self.model.query.order_by(self.model.id.asc()).paginate(page=1, per_page=10).items)

    def test_pagination_sorting_sort_dir_desc(self):
        """
        Test case to check if the correct sorting direction is returned when 'desc' is provided.
        """
        with self.app.test_request_context(query_string='sortDir=desc'):
            result = pagination_sorting(self.model)
            self.assertEqual(result, self.model.query.order_by(self.model.id.desc()).paginate(page=1, per_page=10).items)

    def test_pagination_sorting_search_params(self):
        """
        Test case to check if the correct search parameters are used.
        """
        with self.app.test_request_context(query_string='search=test'):
            result = pagination_sorting(self.model)
            self.assertEqual(result, self.model.query.filter(self.model.name.like('%test%')).order_by(self.model.id).paginate(page=1, per_page=10).items)

if __name__ == '__main__':
    unittest.main()