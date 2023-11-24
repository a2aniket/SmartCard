from python-flask-server.openapi_server.controllers.security_controller_ import *
import unittest
from unittest.mock import patch, MagicMock
from openapi_server import app
from openapi_server.services.user_service import UserService
from openapi_server.models.user import User
from datetime import datetime, timedelta
import jwt


class TestAuthentication(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['JWT_SECRET_KEY'] = 'secret'
        app.config['JWT_EXPIRATION_HOURS'] = 24
        app.config['TESTING'] = True

    def test_authenticate_valid_credentials(self):
        with patch.object(UserService, 'get_user_by_username', return_value=User(
                id=1,
                username="testuser",
                password="testpassword"
        )):
            user = authenticate("testuser", "testpassword")
            self.assertIsInstance(user, User)

    def test_authenticate_invalid_credentials(self):
        with patch.object(UserService, 'get_user_by_username', return_value=None):
            user = authenticate("testuser", "testpassword")
            self.assertIsNone(user)

    def test_create_token(self):
        token = create_token(1)
        self.assertIsInstance(token, bytes)

    def test_authorize_valid_token(self):
        expiry_time = datetime.utcnow() + timedelta(hours=24)
        payload = {"sub": 1, "iat": datetime.utcnow(), "exp": expiry_time}
        token = jwt.encode(payload, app.config.get("JWT_SECRET_KEY").encode('utf-8'), algorithm="HS256")
        with patch.object(User, 'query', MagicMock(return_value=User(
                id=1,
                username="testuser",
                password="testpassword"
        ))):
            user = authorize(token)
            self.assertIsInstance(user, User)

    def test_authorize_expired_token(self):
        expiry_time = datetime.utcnow() - timedelta(hours=24)
        payload = {"sub": 1, "iat": datetime.utcnow(), "exp": expiry_time}
        token = jwt.encode(payload, app.config.get("JWT_SECRET_KEY").encode('utf-8'), algorithm="HS256")
        user = authorize(token)
        self.assertIsNone(user)

    def test_authorize_invalid_token(self):
        token = "invalid_token"
        user = authorize(token)
        self.assertIsNone(user)

    def test_login_valid_credentials(self):
        with patch.object(UserService, 'get_user_by_username', return_value=User(
                id=1,
                username="testuser",
                password="testpassword"
        )):
            with app.test_client() as client:
                response = client.post('/login', json={"username": "testuser", "password": "testpassword"})
                data = response.get_json()
                self.assertEqual(response.status_code, 200)
                self.assertIn('token', data)

    def test_login_invalid_credentials(self):
        with patch.object(UserService, 'get_user_by_username', return_value=None):
            with app.test_client() as client:
                response = client.post('/login', json={"username": "testuser", "password": "testpassword"})
                data = response.get_json()
                self.assertEqual(response.status_code, 401)
                self.assertIn('message', data)


if __name__ == '__main__':
    unittest.main()