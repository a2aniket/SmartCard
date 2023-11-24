from python-flask-server.openapi_server.controllers.user_controller import *
import unittest
from openapi_server import app


class TestUserAPI(unittest.TestCase):
    
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_create_user(self):
        data = {'username': 'test_user', 'password': 'password'}
        response = self.app.post('/users', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('test_user', response.json['username'])

    def test_create_user_missing_data(self):
        data = {'username': 'test_user'}
        response = self.app.post('/users', json=data)
        self.assertEqual(response.status_code, 400)

    def test_get_user_by_username(self):
        response = self.app.get('/users/test_user')
        self.assertEqual(response.status_code, 200)
        self.assertIn('test_user', response.json['username'])

    def test_get_user_by_username_not_found(self):
        response = self.app.get('/users/nonexistent_user')
        self.assertEqual(response.status_code, 404)
        self.assertIn('User not found', response.json['message'])