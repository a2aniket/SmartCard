from python-flask-server.openapi_server.__main__ import *
import unittest
import connexion
from openapi_server import config_test
from openapi_server.controllers import security_controller_, user_controller

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = config_test.connex_app
        self.client = self.app.test_client()

    def test_create_user(self):
        # Test creating a user
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post('/users', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('user_id', response.json())

    def test_login(self):
        # Test logging in with valid credentials
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post('/login', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json())

        # Test logging in with invalid credentials
        data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post('/login', json=data)
        self.assertEqual(response.status_code, 401)
        self.assertIn('message', response.json())

if __name__ == '__main__':
    unittest.main()