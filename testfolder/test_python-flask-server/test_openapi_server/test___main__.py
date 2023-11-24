from python-flask-server.openapi_server.__main__ import *
import unittest
import requests

class TestAPI(unittest.TestCase):
    
    def test_create_user(self):
        # Test creating a new user
        data = {
            "username": "test_user",
            "password": "test_password"
        }
        response = requests.post("http://localhost:8000/users", json=data)
        self.assertEqual(response.status_code, 201)
    
    def test_create_user_missing_username(self):
        # Test creating a new user with missing username
        data = {
            "password": "test_password"
        }
        response = requests.post("http://localhost:8000/users", json=data)
        self.assertEqual(response.status_code, 400)
    
    def test_create_user_missing_password(self):
        # Test creating a new user with missing password
        data = {
            "username": "test_user"
        }
        response = requests.post("http://localhost:8000/users", json=data)
        self.assertEqual(response.status_code, 400)
    
    def test_login(self):
        # Test logging in with valid credentials
        data = {
            "username": "test_user",
            "password": "test_password"
        }
        response = requests.post("http://localhost:8000/login", json=data)
        self.assertEqual(response.status_code, 200)
    
    def test_login_invalid_credentials(self):
        # Test logging in with invalid credentials
        data = {
            "username": "test_user",
            "password": "wrong_password"
        }
        response = requests.post("http://localhost:8000/login", json=data)
        self.assertEqual(response.status_code, 401)
    
    def test_login_missing_username(self):
        # Test logging in with missing username
        data = {
            "password": "test_password"
        }
        response = requests.post("http://localhost:8000/login", json=data)
        self.assertEqual(response.status_code, 400)
    
    def test_login_missing_password(self):
        # Test logging in with missing password
        data = {
            "username": "test_user"
        }
        response = requests.post("http://localhost:8000/login", json=data)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()