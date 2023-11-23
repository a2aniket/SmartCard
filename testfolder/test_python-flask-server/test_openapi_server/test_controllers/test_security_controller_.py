from python-flask-server.openapi_server.controllers.security_controller_ import *
import unittest
from unittest.mock import patch, MagicMock
from openapi_server import app, db
from openapi_server.models.user import User
from openapi_server.services.user_service import UserService
import jwt

class TestAuthentication(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_authenticate_valid_user(self):
        with patch.object(UserService, 'get_user_by_username') as mock_get_user:
            mock_user = MagicMock()
            mock_user.check_password.return_value = True
            mock_get_user.return_value = mock_user

            user = authenticate("test_user", "test_password")

            self.assertEqual(user, mock_user)

    def test_authenticate_invalid_user(self):
        with patch.object(UserService, 'get_user_by_username') as mock_get_user:
            mock_get_user.return_value = None

            user = authenticate("test_user", "test_password")

            self.assertIsNone(user)

    def test_create_token(self):
        app.config['JWT_SECRET_KEY'] = 'test_secret_key'
        app.config['JWT_EXPIRATION_HOURS'] = 24

        user_id = 1
        token = create_token(user_id)

        self.assertIsNotNone(token)

        payload = jwt.decode(token, 'test_secret_key', algorithms=["HS256"])

        self.assertEqual(payload['sub'], user_id)

    def test_authorize_valid_token(self):
        app.config['JWT_SECRET_KEY'] = 'test_secret_key'

        user_id = 1
        token = jwt.encode({'sub': user_id}, 'test_secret_key', algorithm='HS256')

        with patch.object(User, 'query') as mock_query:
            mock_user = MagicMock()
            mock_query.get.return_value = mock_user

            user = authorize(token)

            self.assertEqual(user, mock_user)

    def test_authorize_expired_token(self):
        app.config['JWT_SECRET_KEY'] = 'test_secret_key'

        token = jwt.encode({'exp': datetime.utcnow() - timedelta(hours=1)}, 'test_secret_key', algorithm='HS256')

        user = authorize(token)

        self.assertIsNone(user)

    def test_authorize_invalid_token(self):
        app.config['JWT_SECRET_KEY'] = 'test_secret_key'

        token = "invalid_token"

        user = authorize(token)

        self.assertIsNone(user)

    def test_login_valid_user(self):
        app.config['JWT_SECRET_KEY'] = 'test_secret_key'
        app.config['JWT_EXPIRATION_HOURS'] = 24

        mock_user = MagicMock()
        mock_user.id = 1

        with patch.object(UserService, 'get_user_by_username') as mock_get_user:
            mock_user.check_password.return_value = True
            mock_get_user.return_value = mock_user

            response = self.app.post('/login', json={'username': 'test_user', 'password': 'test_password'})

            self.assertEqual(response.status_code, 200)

            data = response.get_json()

            self.assertIn('token', data)

            token = data['token']

            payload = jwt.decode(token, 'test_secret_key', algorithms=["HS256"])

            self.assertEqual(payload['sub'], mock_user.id)

    def test_login_invalid_user(self):
        with patch.object(UserService, 'get_user_by_username') as mock_get_user:
            mock_get_user.return_value = None

            response = self.app.post('/login', json={'username': 'test_user', 'password': 'test_password'})

            self.assertEqual(response.status_code, 401)

            data = response.get_json()

            self.assertIn('message', data)

            message = data['message']

            self.assertEqual(message, 'Invalid username or password')