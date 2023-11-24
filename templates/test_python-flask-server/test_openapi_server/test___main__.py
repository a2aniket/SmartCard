from python-flask-server.openapi_server.__main__ import *
import unittest
from openapi_server import config_test
from openapi_server.controllers import security_controller_, user_controller

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = config_test.connex_app.test_client()

    def test_create_user_endpoint(self):
        # Test create user endpoint with valid data
        response = self.app.post('/users', json={'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 201)

        # Test create user endpoint with invalid data
        response = self.app.post('/users', json={'username': '', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 400)

    def test_login_endpoint(self):
        # Test login endpoint with valid credentials
        response = self.app.post('/login', json={'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)

        # Test login endpoint with invalid credentials
        response = self.app.post('/login', json={'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()