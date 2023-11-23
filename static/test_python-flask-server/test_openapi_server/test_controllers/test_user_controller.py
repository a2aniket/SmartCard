from python-flask-server.openapi_server.controllers.user_controller import *
import unittest
from openapi_server import app


class TestUserService(unittest.TestCase):

    def test_create_user(self):
        # Test creating a user
        with app.test_client() as client:
            data = {'username': 'test_user', 'password': 'test_password'}
            response = client.post('/users', json=data)
            self.assertEqual(response.status_code, 201)

    def test_get_user_by_username(self):
        # Test getting a user by username
        with app.test_client() as client:
            username = 'test_user'
            response = client.get(f'/users/{username}')
            self.assertEqual(response.status_code, 200)

    def test_get_user_by_username_not_found(self):
        # Test getting a user by username that does not exist
        with app.test_client() as client:
            username = 'non_existent_user'
            response = client.get(f'/users/{username}')
            self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()