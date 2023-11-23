from python-flask-server.openapi_server.controllers.security_controller_ import *
import unittest
from unittest.mock import patch, MagicMock
from openapi_server import app
from openapi_server.models.user import User
from openapi_server.services.user_service import UserService

class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.user = User(username="testuser", password="testpassword")
        UserService.add_user(self.user)

    def tearDown(self):
        UserService.delete_user_by_id(self.user.id)

    def test_successful_authentication(self):
        response = self.app.post('/login', json={"username": "testuser", "password": "testpassword"})
        self.assertEqual(response.status_code, 200)
        self.assertTrue("token" in response.json)

    def test_invalid_username(self):
        response = self.app.post('/login', json={"username": "invaliduser", "password": "testpassword"})
        self.assertEqual(response.status_code, 401)
        self.assertTrue("message" in response.json)
        self.assertEqual(response.json["message"], "Invalid username or password")

    def test_invalid_password(self):
        response = self.app.post('/login', json={"username": "testuser", "password": "invalidpassword"})
        self.assertEqual(response.status_code, 401)
        self.assertTrue("message" in response.json)
        self.assertEqual(response.json["message"], "Invalid username or password")

    @patch("openapi_server.services.user_service.UserService.get_user_by_username")
    def test_authenticate_function(self, mock_get_user_by_username):
        mock_get_user_by_username.return_value = self.user
        result = authenticate("testuser", "testpassword")
        self.assertEqual(result, self.user)

    @patch("openapi_server.services.user_service.UserService.get_user_by_username")
    def test_authenticate_function_with_invalid_username(self, mock_get_user_by_username):
        mock_get_user_by_username.return_value = None
        result = authenticate("invaliduser", "testpassword")
        self.assertIsNone(result)

    @patch("openapi_server.services.user_service.UserService.get_user_by_username")
    def test_authenticate_function_with_invalid_password(self, mock_get_user_by_username):
        mock_user = MagicMock()
        mock_user.check_password.return_value = False
        mock_get_user_by_username.return_value = mock_user
        result = authenticate("testuser", "invalidpassword")
        self.assertIsNone(result)

    def test_create_token_function(self):
        token = create_token(self.user.id)
        self.assertIsNotNone(token)

    def test_authorize_function_with_valid_token(self):
        token = create_token(self.user.id)
        response = self.app.get('/test', headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "Authorized")

    def test_authorize_function_with_expired_token(self):
        expires = datetime.utcnow() - timedelta(hours=1)
        payload = {
            "sub": self.user.id,
            "iat": datetime.utcnow(),
            "exp": expires
        }
        token = jwt.encode(payload, app.config.get("JWT_SECRET_KEY").encode('utf-8'), algorithm="HS256")
        response = self.app.get('/test', headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 401)

    def test_authorize_function_with_invalid_token(self):
        response = self.app.get('/test', headers={"Authorization": "Bearer invalidtoken"})
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()