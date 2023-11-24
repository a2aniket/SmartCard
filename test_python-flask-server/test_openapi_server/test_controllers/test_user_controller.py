from python-flask-server.openapi_server.controllers.user_controller import *
import unittest
from openapi_server import app


class TestUserRoutes(unittest.TestCase):
    
    def test_create_user(self):
        # Test creating a new user
        with app.test_client() as client:
            response = client.post('/users', json={'username': 'test_user', 'password': 'test_password'})
            self.assertEqual(response.status_code, 201)
    
    def test_create_user_missing_data(self):
        # Test creating a new user with missing data
        with app.test_client() as client:
            response = client.post('/users', json={'username': 'test_user'})
            self.assertEqual(response.status_code, 400)
    
    def test_get_user_by_username(self):
        # Test getting a user by their username
        with app.test_client() as client:
            response = client.get('/users/test_user')
            self.assertEqual(response.status_code, 200)
    
    def test_get_user_by_invalid_username(self):
        # Test getting a user with an invalid username
        with app.test_client() as client:
            response = client.get('/users/invalid_username')
            self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()