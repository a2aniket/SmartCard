from python-flask-server.openapi_server.__main__ import *
import unittest
import requests

class TestAPI(unittest.TestCase):

    def test_create_user(self):
        # Test valid user creation
        response = requests.post('http://localhost:8000/users', json={'username': 'test_user', 'password': 'Test1234'})
        self.assertEqual(response.status_code, 201)

        # Test invalid user creation with missing username
        response = requests.post('http://localhost:8000/users', json={'password': 'Test1234'})
        self.assertEqual(response.status_code, 400)

        # Test invalid user creation with missing password
        response = requests.post('http://localhost:8000/users', json={'username': 'test_user'})
        self.assertEqual(response.status_code, 400)

        # Test invalid user creation with existing username
        response = requests.post('http://localhost:8000/users', json={'username': 'test_user', 'password': 'Test1234'})
        self.assertEqual(response.status_code, 409)

    def test_login(self):
        # Test valid login
        response = requests.post('http://localhost:8000/login', json={'username': 'test_user', 'password': 'Test1234'})
        self.assertEqual(response.status_code, 200)

        # Test invalid login with missing username
        response = requests.post('http://localhost:8000/login', json={'password': 'Test1234'})
        self.assertEqual(response.status_code, 400)

        # Test invalid login with missing password
        response = requests.post('http://localhost:8000/login', json={'username': 'test_user'})
        self.assertEqual(response.status_code, 400)

        # Test invalid login with wrong password
        response = requests.post('http://localhost:8000/login', json={'username': 'test_user', 'password': 'WrongPassword'})
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()