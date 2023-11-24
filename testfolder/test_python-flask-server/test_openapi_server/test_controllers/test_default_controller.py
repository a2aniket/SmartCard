from python-flask-server.openapi_server.controllers.default_controller import *
import unittest
import json
from openapi_server.config_test import app

class TestGenerateCodePost(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_generate_code_post(self):
        # Test with valid request payload
        payload = {"input": "test_input"}
        response = self.client.post('/v1/apigen/generate/code', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "This method is not implemented as a service!")

        # Test with invalid request payload
        payload = {"invalid_key": "test_input"}
        response = self.client.post('/v1/apigen/generate/code', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_data(as_text=True), "Bad Request")

        # Test with empty request payload
        payload = {}
        response = self.client.post('/v1/apigen/generate/code', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_data(as_text=True), "Bad Request")