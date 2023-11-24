from python-flask-server.openapi_server.controllers.user_controller import *
import unittest
from unittest.mock import patch
from openapi_server import app


class TestUserAPI(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_create_user_success(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.app.post('/users', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('testuser', response.get_data(as_text=True))

    def test_create_user_missing_data(self):
        data = {'username': 'testuser'}
        response = self.app.post('/users', json=data)
        self.assertEqual(response.status_code, 400)

    def test_get_user_by_username_success(self):
        with patch('openapi_server.services.user_service.UserService.get_user_by_username') as mock_get_user:
            mock_get_user.return_value = {'username': 'testuser', 'password': 'testpassword'}
            response = self.app.get('/users/testuser')
            self.assertEqual(response.status_code, 200)
            self.assertIn('testuser', response.get_data(as_text=True))

    def test_get_user_by_username_not_found(self):
        with patch('openapi_server.services.user_service.UserService.get_user_by_username') as mock_get_user:
            mock_get_user.return_value = None
            response = self.app.get('/users/testuser')
            self.assertEqual(response.status_code, 404)
            self.assertIn('User not found', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()