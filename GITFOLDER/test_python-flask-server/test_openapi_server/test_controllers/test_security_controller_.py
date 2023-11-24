from python-flask-server.openapi_server.controllers.security_controller_ import *
import unittest
from unittest.mock import patch, MagicMock
from openapi_server import app
from openapi_server.models.user import User
from openapi_server.services.user_service import UserService
import jwt
from datetime import datetime, timedelta

class TestAuth(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_authenticate(self):
        with patch.object(UserService, 'get_user_by_username') as mock_get_user:
            mock_user = MagicMock()
            mock_user.check_password.return_value = True
            mock_get_user.return_value = mock_user
            result = authenticate("testUser", "testPassword")
            self.assertEqual(result, mock_user)

    def test_create_token(self):
        with app.app_context():
            app.config['JWT_SECRET_KEY'] = 'test_secret_key'
            app.config['JWT_EXPIRATION_HOURS'] = 24
            user_id = 1
            token = create_token(user_id)
            self.assertTrue(token)

    def test_authorize(self):
        with app.app_context():
            app.config['JWT_SECRET_KEY'] = 'test_secret_key'
            app.config['JWT_EXPIRATION_HOURS'] = 24
            user_id = 1
            token = jwt.encode({'sub': user_id, 'exp': datetime.utcnow() + timedelta(hours=24)}, app.config['JWT_SECRET_KEY'], algorithm='HS256')
            user = User(username='testUser', password='testPassword')
            user.id = user_id
            with patch.object(User, 'query') as mock_query:
                mock_query.get.return_value = user
                result = authorize(token)
                self.assertEqual(result, user)

    def test_login_success(self):
        with app.app_context():
            app.config['JWT_SECRET_KEY'] = 'test_secret_key'
            app.config['JWT_EXPIRATION_HOURS'] = 24
            user = User(username='testUser', password='testPassword')
            with patch.object(UserService, 'get_user_by_username') as mock_get_user:
                mock_get_user.return_value = user
                response = self.app.post('/api/login', json={'username': 'testUser', 'password': 'testPassword'})
                self.assertEqual(response.status_code, 200)
                self.assertIn('token', response.json)

    def test_login_failure(self):
        with app.app_context():
            with patch.object(UserService, 'get_user_by_username') as mock_get_user:
                mock_get_user.return_value = None
                response = self.app.post('/api/login', json={'username': 'testUser', 'password': 'testPassword'})
                self.assertEqual(response.status_code, 401)
                self.assertIn('message', response.json)