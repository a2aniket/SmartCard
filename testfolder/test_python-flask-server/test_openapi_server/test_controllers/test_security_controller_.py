from python-flask-server.openapi_server.controllers.security_controller_ import *
import unittest
from unittest.mock import MagicMock
from openapi_server import app
from datetime import datetime, timedelta

class TestAuth(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()

        # Set the JWT secret key and expiration time
        app.config["JWT_SECRET_KEY"] = "test_secret_key"
        app.config["JWT_EXPIRATION_HOURS"] = 24

        # Create a test user object
        self.user = MagicMock()
        self.user.id = 1
        self.user.check_password.return_value = True
        self.user_query = MagicMock()
        self.user_query.get.return_value = self.user
        self.user_service = MagicMock()
        self.user_service.get_user_by_username.return_value = self.user

    def test_authenticate_valid_user(self):
        # Test for valid user authentication
        user = authenticate("test_user", "test_password")
        self.assertEqual(user, self.user)

    def test_authenticate_invalid_user(self):
        # Test for invalid user authentication
        user = authenticate("invalid_user", "invalid_password")
        self.assertIsNone(user)

    def test_create_token(self):
        # Test for token generation
        expected_token = jwt.encode({
            "sub": 1,
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(hours=24)
        }, "test_secret_key".encode('utf-8'), algorithm="HS256")
        token = create_token(self.user.id)
        self.assertEqual(token, expected_token)

    def test_authorize_valid_token(self):
        # Test for valid token authorization
        token = create_token(self.user.id)
        with app.app_context():
            user = authorize(token)
        self.assertEqual(user, self.user)

    def test_authorize_expired_token(self):
        # Test for expired token authorization
        expired_token = jwt.encode({
            "sub": 1,
            "iat": datetime.utcnow() - timedelta(hours=24),
            "exp": datetime.utcnow() - timedelta(hours=12)
        }, "test_secret_key".encode('utf-8'), algorithm="HS256")
        with app.app_context():
            user = authorize(expired_token)
        self.assertIsNone(user)

    def test_authorize_invalid_token(self):
        # Test for invalid token authorization
        invalid_token = "invalid_token"
        with app.app_context():
            user = authorize(invalid_token)
        self.assertIsNone(user)

    def test_login_valid_credentials(self):
        # Test for valid user login credentials
        self.user_service.get_user_by_username.return_value = self.user
        response = self.app.post("/login", json={"username": "test_user", "password": "test_password"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.json)

    def test_login_invalid_credentials(self):
        # Test for invalid user login credentials
        self.user_service.get_user_by_username.return_value = None
        response = self.app.post("/login", json={"username": "invalid_user", "password": "invalid_password"})
        self.assertEqual(response.status_code, 401)
        self.assertIn("message", response.json)