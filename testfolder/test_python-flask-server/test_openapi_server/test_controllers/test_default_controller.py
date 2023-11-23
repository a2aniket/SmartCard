from python-flask-server.openapi_server.controllers.default_controller import *
import unittest
import json

from openapi_server.config_test import app

class TestGenerateCodePost(unittest.TestCase):

    def test_generate_code_post(self):
        with app.test_client() as client:
            # Test with valid request
            data = {
                "input": "test_input"
            }
            response = client.post('/v1/apigen/generate/code', data=json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_data(as_text=True), "This method is not implemented as a service!")

            # Test with invalid request
            data = {
                "invalid_key": "invalid_value"
            }
            response = client.post('/v1/apigen/generate/code', data=json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.get_json(), {"error": "Bad request"})

if __name__ == '__main__':
    unittest.main()