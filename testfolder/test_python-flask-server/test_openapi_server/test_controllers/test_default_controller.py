from python-flask-server.openapi_server.controllers.default_controller import *
import unittest
import json
from openapi_server.config_test import app

class TestGenerateCodePost(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_generate_code_post(self):
        """
        Test that generate_code_post returns correct response
        """
        data = {"input": "some_input"}
        response = self.app.post('/v1/apigen/generate/code', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "This method is not implemented as a service!")

    def test_generate_code_post_invalid_input(self):
        """
        Test that generate_code_post returns error for invalid input
        """
        data = {"invalid_input": "some_input"}
        response = self.app.post('/v1/apigen/generate/code', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()