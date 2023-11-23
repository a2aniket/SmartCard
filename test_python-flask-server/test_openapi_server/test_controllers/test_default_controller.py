from python-flask-server.openapi_server.controllers.default_controller import *
import unittest
import json
from openapi_server.config_test import app
from openapi_server.services.default_service import DefaultService

class TestGenerateCodePost(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_generate_code_post(self):
        input_data = {'data': 'test_data'}
        response = self.app.post('/v1/apigen/generate/code', data=json.dumps(input_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'This method is not implemented as a service!')