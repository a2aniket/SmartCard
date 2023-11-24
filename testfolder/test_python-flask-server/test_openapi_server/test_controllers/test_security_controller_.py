from python-flask-server.openapi_server.controllers.security_controller_ import *
import unittest
from unittest.mock import patch, MagicMock
from openapi_server import app
from openapi_server.services.user_service import UserService

class TestAuthentication(unittest.TestCase):
    @patch('openapi_server.routes.authenticate')
    def test_login_success(self, mock_authenticate):
        mock_authenticate.return_value = MagicMock()
        mock_authenticate.return_value.id = 1
        mock_authenticate.return_value.username = 'testuser'
        mock_authenticate.return_value.check_password.return_value = True

        with app.test_client() as client:
            response = client.post('/login', json={"username": "testuser", "password": "testpassword"})
            self.assertEqual(response.status_code, 200)
            self.assertIn('token', response.json)

    @patch('openapi_server.routes.authenticate')
    def test_login_failure(self, mock_authenticate):
        mock_authenticate.return_value = None

        with app.test_client() as client:
            response = client.post('/login', json={"username": "testuser", "password": "testpassword"})
            self.assertEqual(response.status_code, 401)
            self.assertIn('message', response.json)
            self.assertEqual(response.json['message'], 'Invalid username or password')

    @patch.object(UserService, 'get_user_by_username')
    def test_authenticate_success(self, mock_get_user_by_username):
        mock_user = MagicMock()
        mock_user.check_password.return_value = True
        mock_get_user_by_username.return_value = mock_user

        user = authenticate('testuser', 'testpassword')
        self.assertIsNotNone(user)

    @patch.object(UserService, 'get_user_by_username')
    def test_authenticate_failure(self, mock_get_user_by_username):
        mock_get_user_by_username.return_value = None

        user = authenticate('testuser', 'testpassword')
        self.assertIsNone(user)

    @patch('openapi_server.routes.jwt.encode')
    def test_create_token(self, mock_encode):
        mock_encode.return_value = 'test_token'

        token = create_token(1)
        self.assertEqual(token, 'test_token')

    @patch('openapi_server.routes.jwt.decode')
    def test_authorize_success(self, mock_decode):
        mock_decode.return_value = {'sub': 1}
        mock_user = MagicMock()
        mock_user.id = 1
        User.query.get.return_value = mock_user

        user = authorize('test_token')
        self.assertIsNotNone(user)

    @patch('openapi_server.routes.jwt.decode')
    def test_authorize_expired_token(self, mock_decode):
        mock_decode.side_effect = jwt.ExpiredSignatureError

        user = authorize('test_token')
        self.assertIsNone(user)

    @patch('openapi_server.routes.jwt.decode')
    def test_authorize_invalid_token(self, mock_decode):
        mock_decode.side_effect = jwt.InvalidTokenError

        user = authorize('test_token')
        self.assertIsNone(user)