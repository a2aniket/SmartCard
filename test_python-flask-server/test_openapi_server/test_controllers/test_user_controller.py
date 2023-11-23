from python-flask-server.openapi_server.controllers.user_controller import *
import unittest
from openapi_server.services.user_service import UserService
from openapi_server import app


class TestUserService(unittest.TestCase):

    def test_create_user(self):
        # Test creating a user with valid data
        data = {'username': 'test_user', 'password': 'test_password'}
        response = app.test_client().post('/users', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(response.json.get('id'))

        # Test creating a user with invalid data
        data = {'username': '', 'password': 'test_password'}
        response = app.test_client().post('/users', json=data)
        self.assertEqual(response.status_code, 400)

    def test_get_user_by_username(self):
        # Test getting an existing user
        user = UserService.create_user('test_user', 'test_password')
        response = app.test_client().get(f"/users/{user.username}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json.get('username'), user.username)

        # Test getting a non-existent user
        response = app.test_client().get('/users/non_existent_user')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()