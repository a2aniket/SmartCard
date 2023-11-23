from python-flask-server.openapi_server.__main__ import *
import unittest
from unittest.mock import patch

import connexion
from openapi_server import config_test
from openapi_server.controllers import security_controller_, user_controller


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = connexion.app.test_client()

    def test_create_user(self):
        with patch.object(user_controller, 'create_user', return_value={'id': 1}) as mock_method:
            response = self.client.post('/users', json={'username': 'test', 'password': 'password'})
            mock_method.assert_called_once_with({'username': 'test', 'password': 'password'})
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json, {'id': 1})

    def test_login(self):
        with patch.object(security_controller_, 'login', return_value={'access_token': 'token'}) as mock_method:
            response = self.client.post('/login', json={'username': 'test', 'password': 'password'})
            mock_method.assert_called_once_with('test', 'password')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'access_token': 'token'})

if __name__ == '__main__':
    unittest.main()