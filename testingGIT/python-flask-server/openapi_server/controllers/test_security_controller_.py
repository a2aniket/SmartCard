from security_controller_ import *
import unittest
from unittest.mock import patch, Mock
from openapi_server import app
from openapi_server.services.user_service import UserService
from openapi_server.models.user import User

class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch.object(UserService, 'get_user_by_username')
    def test_authenticate_valid_user(self, mock_user_service):
        mock_user = Mock(spec=User)
        mock_user.check_password.return_value = True
        mock_user_service.return_value = mock_user

        result = authenticate('testuser', 'testpassword')
        self.assertEqual(result, mock_user)

    @patch.object(UserService, 'get_user_by_username')
    def test_authenticate_invalid_user(self, mock_user_service):
        mock_user_service.return_value = None

        result = authenticate('invaliduser', 'invalidpassword')
        self.assertEqual(result, None)

    def test_create_token(self):
        with app.app_context():
            app.config['JWT_SECRET_KEY'] = 'testsecret'
            app.config['JWT_EXPIRATION_HOURS'] = 1
            token = create_token(1)
            self.assertTrue(isinstance(token, bytes))

    @patch('openapi_server.authentication.jwt.decode')
    def test_authorize_valid_token(self, mock_jwt_decode):
        mock_user = Mock(spec=User)
        mock_user.id = 1
        mock_jwt_decode.return_value = {'sub': 1}
        with app.app_context():
            user = authorize('validtoken')
            self.assertEqual(user, mock_user)

    @patch('openapi_server.authentication.jwt.decode')
    def test_authorize_expired_token(self, mock_jwt_decode):
        mock_jwt_decode.side_effect = jwt.ExpiredSignatureError
        with app.app_context():
            user = authorize('expiredtoken')
            self.assertEqual(user, None)

    @patch('openapi_server.authentication.jwt.decode')
    def test_authorize_invalid_token(self, mock_jwt_decode):
        mock_jwt_decode.side_effect = jwt.InvalidTokenError
        with app.app_context():
            user = authorize('invalidtoken')
            self.assertEqual(user, None)

    def test_login_valid_user(self):
        with app.app_context():
            mock_user = Mock(spec=User)
            mock_user.id = 1
            mock_user.check_password.return_value = True
            UserService.get_user_by_username.return_value = mock_user
            response = self.app.post('/login', json={'username': 'testuser', 'password': 'testpassword'})
            self.assertEqual(response.status_code, 200)
            self.assertTrue('token' in response.json)

    def test_login_invalid_user(self):
        with app.app_context():
            UserService.get_user_by_username.return_value = None
            response = self.app.post('/login', json={'username': 'invaliduser', 'password': 'invalidpassword'})
            self.assertEqual(response.status_code, 401)
            self.assertTrue('message' in response.json)