from python-flask-server.openapi_server.controllers.default_controller import *
import unittest
import json
from openapi_server.config_test import app


class TestGenerateCodePost(unittest.TestCase):

    def test_generate_code_post_success(self):
        """
        Test generate_code_post API with valid input
        """
        with app.test_client() as client:
            data = {"input": "valid_input"}
            response = client.post('/v1/apigen/generate/code', data=json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_data(as_text=True), "This method is not implemented as a service!")

    def test_generate_code_post_invalid_input(self):
        """
        Test generate_code_post API with invalid input
        """
        with app.test_client() as client:
            data = {"input": None}
            response = client.post('/v1/apigen/generate/code', data=json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.get_data(as_text=True), "Invalid input provided!")

    def test_generate_code_post_invalid_content_type(self):
        """
        Test generate_code_post API with invalid content type
        """
        with app.test_client() as client:
            data = {"input": "valid_input"}
            response = client.post('/v1/apigen/generate/code', data=json.dumps(data), content_type='text/plain')
            self.assertEqual(response.status_code, 415)
            self.assertEqual(response.get_data(as_text=True), "Unsupported media type. Please use application/json!")

    def test_generate_code_post_missing_input_key(self):
        """
        Test generate_code_post API with missing input key
        """
        with app.test_client() as client:
            data = {"invalid_key": "valid_input"}
            response = client.post('/v1/apigen/generate/code', data=json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.get_data(as_text=True), "Input key missing!")

    def test_generate_code_post_empty_input_value(self):
        """
        Test generate_code_post API with empty input value
        """
        with app.test_client() as client:
            data = {"input": ""}
            response = client.post('/v1/apigen/generate/code', data=json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.get_data(as_text=True), "Empty input value provided!")

if __name__ == '__main__':
    unittest.main()