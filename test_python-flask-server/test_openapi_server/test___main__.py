from python-flask-server.openapi_server.__main__ import *
import unittest
import requests
from unittest.mock import patch, MagicMock
from openapi_server.controllers import security_controller_, user_controller

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_create_user(self):
        response = self.app.post('/users', json={"username": "test_user", "password": "test_password"})
        self.assertEqual(response.status_code, 201)

    def test_create_user_with_existing_username(self):
        response1 = self.app.post('/users', json={"username": "existing_user", "password": "test_password"})
        response2 = self.app.post('/users', json={"username": "existing_user", "password": "test_password"})
        self.assertEqual(response2.status_code, 409)

    def test_login(self):
        response = self.app.post('/login', json={"username": "test_user", "password": "test_password"})
        self.assertEqual(response.status_code, 200)

    def test_login_with_invalid_credentials(self):
        response = self.app.post('/login', json={"username": "test_user", "password": "invalid_password"})
        self.assertEqual(response.status_code, 401)

    @patch('openapi_server.controllers.security_controller_.authenticate')
    def test_login_with_mocked_authenticate(self, mock_authenticate):
        mock_authenticate.return_value = {"username": "test_user", "password": "test_password"}
        response = self.app.post('/login', json={"username": "test_user", "password": "test_password"})
        self.assertEqual(response.status_code, 200)

    @patch('openapi_server.controllers.user_controller.create_user')
    def test_create_user_with_mocked_create_user(self, mock_create_user):
        mock_create_user.return_value = MagicMock(status_code=201)
        response = self.app.post('/users', json={"username": "test_user", "password": "test_password"})
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()