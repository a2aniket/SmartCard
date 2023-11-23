from python-flask-server.openapi_server.controllers.user_controller import *
import unittest
from openapi_server import app


class TestUserEndpoints(unittest.TestCase):

    def test_create_user(self):
        with app.test_client() as client:
            # Test creating a user successfully
            user_data = {'username': 'test_user', 'password': 'password'}
            response = client.post('/users', json=user_data)
            self.assertEqual(response.status_code, 201)
            self.assertIn('test_user', str(response.data))

            # Test creating a user with missing data
            user_data = {'username': 'test_user'}
            response = client.post('/users', json=user_data)
            self.assertEqual(response.status_code, 400)
            self.assertIn('error', str(response.data))

    def test_get_user_by_username(self):
        with app.test_client() as client:
            # Test getting an existing user
            response = client.get('/users/test_user')
            self.assertEqual(response.status_code, 200)
            self.assertIn('test_user', str(response.data))

            # Test getting a non-existing user
            response = client.get('/users/non_existing_user')
            self.assertEqual(response.status_code, 404)
            self.assertIn('User not found', str(response.data))


if __name__ == '__main__':
    unittest.main()