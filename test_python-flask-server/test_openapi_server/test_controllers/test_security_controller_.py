from python-flask-server.openapi_server.controllers.security_controller_ import *
import unittest
from unittest.mock import MagicMock, patch
from openapi_server import app
from openapi_server.services.user_service import UserService
from openapi_server.models.user import User

class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.user = User(username="testuser", password="testpassword")

    def tearDown(self):
        UserService.delete_user_by_username(self.user.username)

    def test_authenticate_valid_user(self):
        UserService.create_user(self.user)
        authenticated_user = authenticate(self.user.username, self.user.password)
        self.assertIsNotNone(authenticated_user)
        self.assertEqual(authenticated_user.username, self.user.username)

    def test_authenticate_invalid_user(self):
        UserService.create_user(self.user)
        authenticated_user = authenticate(self.user.username, "wrongpassword")
        self.assertIsNone(authenticated_user)

    def test_create_token(self):
        token = create_token(self.user.id)
        self.assertIsNotNone(token)

    def test_authorize_valid_token(self):
        UserService.create_user(self.user)
        token = create_token(self.user.id)
        authorized_user = authorize(token)
        self.assertIsNotNone(authorized_user)
        self.assertEqual(authorized_user.username, self.user.username)

    def test_authorize_expired_token(self):
        UserService.create_user(self.user)
        app.config["JWT_EXPIRATION_HOURS"] = -1
        token = create_token(self.user.id)
        authorized_user = authorize(token)
        self.assertIsNone(authorized_user)

    def test_authorize_invalid_token(self):
        UserService.create_user(self.user)
        token = create_token(self.user.id)
        with patch("jwt.decode", side_effect=jwt.InvalidTokenError):
            authorized_user = authorize(token)
        self.assertIsNone(authorized_user)

    def test_login_valid_credentials(self):
        UserService.create_user(self.user)
        response = self.app.post("/login", json={"username": self.user.username, "password": self.user.password})
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.json)

    def test_login_invalid_credentials(self):
        UserService.create_user(self.user)
        response = self.app.post("/login", json={"username": self.user.username, "password": "wrongpassword"})
        self.assertEqual(response.status_code, 401)
        self.assertIn("message", response.json)