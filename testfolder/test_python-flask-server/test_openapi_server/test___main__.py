from python-flask-server.openapi_server.__main__ import *
import unittest
import json
from openapi_server import app

class TestApp(unittest.TestCase):
    
    def test_create_user(self):
        # Test creating a new user
        with app.test_client() as client:
            # Create a sample user
            user = {
                "username": "testuser",
                "password": "testpassword",
                "email": "testuser@example.com"
            }
            # Send a POST request to create the user
            response = client.post('/users', data=json.dumps(user), content_type='application/json')
            # Check that the response is valid and the user was created
            self.assertEqual(response.status_code, 201)
            self.assertIn('id', response.json)
            # Delete the user to clean up after the test
            user_id = response.json['id']
            client.delete(f'/users/{user_id}')
    
    def test_create_user_duplicate_username(self):
        # Test creating a new user with a duplicate username
        with app.test_client() as client:
            # Create a sample user
            user = {
                "username": "testuser",
                "password": "testpassword",
                "email": "testuser@example.com"
            }
            # Send a POST request to create the user
            client.post('/users', data=json.dumps(user), content_type='application/json')
            # Send another POST request with the same username
            response = client.post('/users', data=json.dumps(user), content_type='application/json')
            # Check that the response is a bad request with an error message
            self.assertEqual(response.status_code, 400)
            self.assertIn('error', response.json)
            # Delete the user to clean up after the test
            user_id = response.json['id']
            client.delete(f'/users/{user_id}')
    
    def test_create_user_missing_username(self):
        # Test creating a new user with a missing username
        with app.test_client() as client:
            # Create a sample user with a missing username
            user = {
                "password": "testpassword",
                "email": "testuser@example.com"
            }
            # Send a POST request to create the user
            response = client.post('/users', data=json.dumps(user), content_type='application/json')
            # Check that the response is a bad request with an error message
            self.assertEqual(response.status_code, 400)
            self.assertIn('error', response.json)
    
    def test_login(self):
        # Test logging in with a valid user
        with app.test_client() as client:
            # Create a sample user
            user = {
                "username": "testuser",
                "password": "testpassword",
                "email": "testuser@example.com"
            }
            client.post('/users', data=json.dumps(user), content_type='application/json')
            # Send a POST request to log in with the user's credentials
            login_data = {
                "username": "testuser",
                "password": "testpassword"
            }
            response = client.post('/login', data=json.dumps(login_data), content_type='application/json')
            # Check that the response is valid and includes a token
            self.assertEqual(response.status_code, 200)
            self.assertIn('access_token', response.json)
            # Delete the user to clean up after the test
            user_id = response.json['id']
            client.delete(f'/users/{user_id}')
    
    def test_login_invalid_credentials(self):
        # Test logging in with invalid credentials
        with app.test_client() as client:
            # Create a sample user
            user = {
                "username": "testuser",
                "password": "testpassword",
                "email": "testuser@example.com"
            }
            client.post('/users', data=json.dumps(user), content_type='application/json')
            # Send a POST request to log in with incorrect credentials
            login_data = {
                "username": "testuser",
                "password": "wrongpassword"
            }
            response = client.post('/login', data=json.dumps(login_data), content_type='application/json')
            # Check that the response is a bad request with an error message
            self.assertEqual(response.status_code, 400)
            self.assertIn('error', response.json)
            # Delete the user to clean up after the test
            user_id = response.json['id']
            client.delete(f'/users/{user_id}')
        
if __name__ == '__main__':
    unittest.main()