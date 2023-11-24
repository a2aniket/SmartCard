from python-flask-server.openapi_server.controllers.default_controller import *
import unittest
import json
from openapi_server.config_test import app


class TestGenerateCodePost(unittest.TestCase):

    def test_generate_code_post_success(self):
        """
        Test generate_code_post with valid JSON request data.
        """
        with app.test_client() as client:
            data = {
                "param1": "value1",
                "param2": "value2"
            }
            response = client.post('/v1/apigen/generate/code', json=data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_data(as_text=True), "This method is not implemented as a service!")

    def test_generate_code_post_invalid_json(self):
        """
        Test generate_code_post with invalid JSON request data.
        """
        with app.test_client() as client:
            data = "invalid json"
            response = client.post('/v1/apigen/generate/code', json=data)
            self.assertEqual(response.status_code, 400)

    def test_generate_code_post_missing_params(self):
        """
        Test generate_code_post with missing parameters in JSON request data.
        """
        with app.test_client() as client:
            data = {
                "param1": "value1"
            }
            response = client.post('/v1/apigen/generate/code', json=data)
            self.assertEqual(response.status_code, 400)