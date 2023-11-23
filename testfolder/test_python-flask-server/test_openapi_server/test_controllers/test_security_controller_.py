from python-flask-server.openapi_server.controllers.security_controller_ import *
import unittest
from unittest.mock import patch, MagicMock

from openapi_server.services.user_service import UserService
from openapi_server.models.user import User
from app import app


class TestAuthentication(unittest.TestCase):
    
    def setUp(self):
        app.config["JWT_SECRET_KEY"] = "testing"
        app.config["JWT_EXPIRATION_HOURS"] = 24
        
        self.client = app.test_client()
        
    def test_authenticate_valid_user(self):
        with patch.object(UserService, "get_user_by_username") as mock_get_user:
            mock_user = MagicMock(spec=User)
            mock_user.check_password.return_value = True
            mock_get_user.return_value = mock_user
            
            user = authenticate("test", "test123")
            
            self.assertEqual(user, mock_user)
            
            mock_get_user.assert_called_once_with("test")
            mock_user.check_password.assert_called_once_with("test123")
            
    def test_authenticate_invalid_user(self):
        with patch.object(UserService, "get_user_by_username") as mock_get_user:
            mock_get_user.return_value = None
            
            user = authenticate("test", "test123")
            
            self.assertIsNone(user)
            
            mock_get_user.assert_called_once_with("test")
            
    def test_create_token(self):
        token = create_token(1)
        
        self.assertIsInstance(token, bytes)
        
        with self.assertRaises(jwt.InvalidTokenError):
            jwt.decode(token, "wrong_secret", algorithms=["HS256"])
            
        with self.assertRaises(jwt.ExpiredSignatureError):
            jwt.decode(token, app.config.get("JWT_SECRET_KEY"), algorithms=["HS256"], options={"verify_exp": False})
            
    def test_authorize_valid_token(self):
        with patch.object(User, "query") as mock_query:
            mock_user = MagicMock(spec=User)
            mock_query.get.return_value = mock_user
            
            token = jwt.encode({"sub": 1, "iat": datetime.utcnow(), "exp": datetime.utcnow() + timedelta(hours=24)}, app.config.get("JWT_SECRET_KEY").encode('utf-8'), algorithm="HS256")
            
            user = authorize(token)
            
            self.assertEqual(user, mock_user)
            
            mock_query.get.assert_called_once_with(1)
            
    def test_authorize_invalid_token(self):
        user = authorize("invalid_token")
        
        self.assertIsNone(user)
        
    def test_login_valid_credentials(self):
        with patch.object(UserService, "get_user_by_username") as mock_get_user:
            mock_user = MagicMock(spec=User)
            mock_user.check_password.return_value = True
            mock_get_user.return_value = mock_user
            
            response = self.client.post("/login", json={"username": "test", "password": "test123"})
            
            self.assertEqual(response.status_code, 200)
            self.assertIn("token", response.json)
            
            mock_get_user.assert_called_once_with("test")
            mock_user.check_password.assert_called_once_with("test123")
            
    def test_login_invalid_credentials(self):
        with patch.object(UserService, "get_user_by_username") as mock_get_user:
            mock_get_user.return_value = None
            
            response = self.client.post("/login", json={"username": "test", "password": "test123"})
            
            self.assertEqual(response.status_code, 401)
            self.assertIn("message", response.json)
            
            mock_get_user.assert_called_once_with("test")