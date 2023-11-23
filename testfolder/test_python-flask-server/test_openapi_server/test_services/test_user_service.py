from python-flask-server.openapi_server.services.user_service import *
import unittest
from unittest.mock import MagicMock
from openapi_server.config_test import db
from openapi_server.models.user import User
from openapi_server.user_service import UserService

class TestUserService(unittest.TestCase):

    def setUp(self):
        db.create_all()
        self.userService = UserService()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_user(self):
        # Test creating a user
        user = self.userService.create_user("john", "password")
        self.assertEqual(user.username, "john")
        self.assertEqual(user.password, "password")

    def test_get_user_by_username(self):
        # Test getting a user by username
        user = self.userService.create_user("john", "password")
        result = self.userService.get_user_by_username("john")
        self.assertEqual(result, user)

    def test_get_user_by_username_not_found(self):
        # Test getting a user by non-existent username
        result = self.userService.get_user_by_username("jane")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()