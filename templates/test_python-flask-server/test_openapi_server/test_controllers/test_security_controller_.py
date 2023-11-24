from python-flask-server.openapi_server.controllers.security_controller_ import *
import unittest
from unittest.mock import patch, MagicMock

from flask import Flask
from werkzeug.exceptions import Unauthorized

from openapi_server.models.user import User
from openapi_server.services.user_service import UserService
from openapi_server.views import auth_views


class AuthViewsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config["JWT_SECRET_KEY"] = "test_secret_key"
        self.app.config["JWT_EXPIRATION_HOURS"] = 24
        self.app.register_blueprint(auth_views.bp)

        self.client = self.app.test_client()

    def test_login_success(self):
        with patch.object(UserService, "get_user_by_username") as mock_get_user_by_username:
            mock_get_user_by_username.return_value = User(id=1, username="test_user", password="test_password")
            with patch("openapi_server.views.auth_views.create_token") as mock_create_token:
                mock_create_token.return_value = "test_token"
                response = self.client.post("/login", json={"username": "test_user", "password": "test_password"})

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json, {"token": "test_token"})

    def test_login_failure(self):
        with patch.object(UserService, "get_user_by_username") as mock_get_user_by_username:
            mock_get_user_by_username.return_value = None
            response = self.client.post("/login", json={"username": "test_user", "password": "test_password"})

            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.json, {"message": "Invalid username or password"})

    def test_authorize_success(self):
        with self.app.test_request_context(headers={"Authorization": "Bearer test_token"}):
            with patch("openapi_server.views.auth_views.User") as mock_user:
                mock_user.query.get.return_value = User(id=1, username="test_user", password="test_password")
                user = auth_views.authorize("test_token")

                self.assertEqual(user.id, 1)
                self.assertEqual(user.username, "test_user")
                self.assertEqual(user.password, "test_password")

    def test_authorize_expired_token(self):
        with self.app.test_request_context(headers={"Authorization": "Bearer test_token"}):
            with patch("openapi_server.views.auth_views.jwt.decode") as mock_decode:
                mock_decode.side_effect = jwt.ExpiredSignatureError
                with self.assertRaises(Unauthorized):
                    auth_views.authorize("test_token")

    def test_authorize_invalid_token(self):
        with self.app.test_request_context(headers={"Authorization": "Bearer test_token"}):
            with patch("openapi_server.views.auth_views.jwt.decode") as mock_decode:
                mock_decode.side_effect = jwt.InvalidTokenError
                with self.assertRaises(Unauthorized):
                    auth_views.authorize("test_token")

    def test_create_token(self):
        with patch("openapi_server.views.auth_views.jwt.encode") as mock_encode:
            mock_encode.return_value = "test_token"
            token = auth_views.create_token(1)

            self.assertEqual(token, "test_token")

    def test_authenticate_success(self):
        with patch.object(UserService, "get_user_by_username") as mock_get_user_by_username:
            mock_user = MagicMock()
            mock_user.check_password.return_value = True
            mock_get_user_by_username.return_value = mock_user
            user = auth_views.authenticate("test_user", "test_password")

            self.assertEqual(user, mock_user)

    def test_authenticate_failure(self):
        with patch.object(UserService, "get_user_by_username") as mock_get_user_by_username:
            mock_user = MagicMock()
            mock_user.check_password.return_value = False
            mock_get_user_by_username.return_value = mock_user
            user = auth_views.authenticate("test_user", "test_password")

            self.assertIsNone(user)