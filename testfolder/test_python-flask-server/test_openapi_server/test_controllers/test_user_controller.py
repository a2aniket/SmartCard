from python-flask-server.openapi_server.controllers.user_controller import *
import unittest
from openapi_server import app


class TestUserAPI(unittest.TestCase):

    def test_create_user(self):
        with app.test_client() as client:
            # Test case 1: Valid request, should return 201 status code and user object
            data = {'username': 'testuser', 'password': 'testpassword'}
            response = client.post('/users', json=data)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json['username'], 'testuser')
            self.assertEqual(response.json['password'], 'testpassword')

            # Test case 2: Invalid request, missing username, should return 400 status code
            data = {'password': 'testpassword'}
            response = client.post('/users', json=data)
            self.assertEqual(response.status_code, 400)

            # Test case 3: Invalid request, missing password, should return 400 status code
            data = {'username': 'testuser'}
            response = client.post('/users', json=data)
            self.assertEqual(response.status_code, 400)

    def test_get_user_by_username(self):
        with app.test_client() as client:
            # Test case 1: Valid username, should return 200 status code and user object
            response = client.get('/users/testuser')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['username'], 'testuser')
            self.assertEqual(response.json['password'], 'testpassword')

            # Test case 2: Invalid username, should return 404 status code and error message
            response = client.get('/users/nonexistentuser')
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json['message'], 'User not found')


if __name__ == '__main__':
    unittest.main()