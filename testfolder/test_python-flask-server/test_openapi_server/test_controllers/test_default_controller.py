from python-flask-server.openapi_server.controllers.default_controller import *
import unittest
from unittest.mock import MagicMock
from openapi_server.config_test import app
from openapi_server.routes.default_controller import generate_code_post


class TestDefaultController(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_generate_code_post(self):
        # Test case for successful response
        response = self.app.post('/v1/apigen/generate/code', json={"test": "data"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "This method is not implemented as a service!")

        # Test case for invalid request
        response = self.app.post('/v1/apigen/generate/code')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), "Bad Request")

        # Test case for internal server error
        with MagicMock():
            response = generate_code_post()
            self.assertEqual(response, "This method is not implemented as a service!")


if __name__ == '__main__':
    unittest.main()