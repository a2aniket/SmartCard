from python-flask-server.openapi_server.__main__ import *
import unittest
import os
import tempfile
import json
from openapi_server import app

class TestAPI(unittest.TestCase):
    # Initialize the test client
    def setUp(self):
        self.app = app.test_client()

    # Test the create user endpoint
    def test_create_user(self):
        # Send a POST request to the create user endpoint with valid user data
        response = self.app.post('/users', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')

        # Check that the response status code is 201 CREATED
        self.assertEqual(response.status_code, 201)

        # Check that the response contains the newly created user's ID
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue('id' in data)

    # Test the login endpoint
    def test_login(self):
        # Send a POST request to the login endpoint with valid user credentials
        response = self.app.post('/login', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the response contains a token
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue('token' in data)

if __name__ == '__main__':
    unittest.main()