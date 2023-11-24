from python-flask-server.openapi_server.__main__ import *
import unittest
import json
from openapi_server import config_test
from openapi_server.controllers import security_controller_, user_controller

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = config_test.connex_app.test_client()

    def test_create_user(self):
        payload = {
            "username": "testuser",
            "password": "testpass"
        }
        response = self.app.post('/users', json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', json.loads(response.data))

    def test_login(self):
        payload = {
            "username": "testuser",
            "password": "testpass"
        }
        response = self.app.post('/login', json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', json.loads(response.data))

if __name__ == '__main__':
    unittest.main()