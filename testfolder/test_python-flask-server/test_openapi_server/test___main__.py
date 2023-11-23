from python-flask-server.openapi_server.__main__ import *
import unittest
from unittest.mock import MagicMock
from openapi_server import config_test
from openapi_server.controllers import security_controller_, user_controller

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = config_test.connex_app.test_client()
        self.app.testing = True

    def test_create_user(self):
        # Test creating a new user
        payload = {"username": "testuser", "password": "testpass"}
        response = self.app.post('/users', json=payload)
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid_input(self):
        # Test creating a new user with invalid input
        payload = {"username": "", "password": "testpass"}
        response = self.app.post('/users', json=payload)
        self.assertEqual(response.status_code, 400)

    def test_login(self):
        # Test user login
        # Mock the login function to return a token
        security_controller_.login = MagicMock(return_value="testtoken")
        payload = {"username": "testuser", "password": "testpass"}
        response = self.app.post('/login', json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["access_token"], "testtoken")

    def test_login_invalid_credentials(self):
        # Test user login with invalid credentials
        # Mock the login function to return None
        security_controller_.login = MagicMock(return_value=None)
        payload = {"username": "testuser", "password": "testpass"}
        response = self.app.post('/login', json=payload)
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()