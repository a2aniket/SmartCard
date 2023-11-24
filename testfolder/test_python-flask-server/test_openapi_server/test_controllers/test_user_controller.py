from python-flask-server.openapi_server.controllers.user_controller import *
import unittest
import json
from openapi_server import app

class TestUserAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.app.post('/users', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_create_user_missing_data(self):
        data = {
            'username': 'testuser'
        }
        response = self.app.post('/users', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_get_user_by_username(self):
        response = self.app.get('/users/testuser')
        self.assertEqual(response.status_code, 200)

    def test_get_user_by_username_not_found(self):
        response = self.app.get('/users/nonexistentuser')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()