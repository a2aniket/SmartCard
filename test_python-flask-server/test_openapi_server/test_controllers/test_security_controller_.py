from python-flask-server.openapi_server.controllers.security_controller_ import *
import unittest
from unittest.mock import patch, MagicMock

from openapi_server import app
from openapi_server.services.user_service import UserService

class TestAuthentication(unittest.TestCase):

    @patch.object(UserService, "get_user_by_username")
    def test_authenticate_valid_user(self, mock_get_user_by_username):
        mock_user = MagicMock()
        mock_user.check_password.return_value = True
        mock_get_user_by_username.return_value = mock_user

        result = authenticate("test_user", "test_password")

        self.assertEqual(result, mock_user)

    @patch.object(UserService, "get_user_by_username")
    def test_authenticate_invalid_user(self, mock_get_user_by_username):
        mock_get_user_by_username.return_value = None

        result = authenticate("test_user", "test_password")

        self.assertIsNone(result)

    @patch("jwt.encode")
    def test_create_token(self, mock_jwt_encode):
        mock_jwt_encode.return_value = b"test_token"

        result = create_token(123)

        self.assertEqual(result, b"test_token")

    @patch("jwt.decode")
    def test_authorize_valid_token(self, mock_jwt_decode):
        mock_user = MagicMock()
        mock_user.id = 123
        mock_jwt_decode.return_value = {"sub": 123}
        User.query.get.return_value = mock_user

        result = authorize("test_token")

        self.assertEqual(result, mock_user)

    @patch("jwt.decode")
    def test_authorize_expired_token(self, mock_jwt_decode):
        mock_jwt_decode.side_effect = jwt.ExpiredSignatureError

        result = authorize("test_token")

        self.assertIsNone(result)

    @patch("jwt.decode")
    def test_authorize_invalid_token(self, mock_jwt_decode):
        mock_jwt_decode.side_effect = jwt.InvalidTokenError

        result = authorize("test_token")

        self.assertIsNone(result)

    def test_login_valid_user(self):
        with app.test_client() as client:
            mock_user = MagicMock()
            mock_user.id = 123
            mock_user.check_password.return_value = True
            UserService.get_user_by_username.return_value = mock_user

            response = client.post("/login", json={"username": "test_user", "password": "test_password"})

            self.assertEqual(response.status_code, 200)
            self.assertIn("token", response.json)

    def test_login_invalid_user(self):
        with app.test_client() as client:
            UserService.get_user_by_username.return_value = None

            response = client.post("/login", json={"username": "test_user", "password": "test_password"})

            self.assertEqual(response.status_code, 401)
            self.assertIn("message", response.json)