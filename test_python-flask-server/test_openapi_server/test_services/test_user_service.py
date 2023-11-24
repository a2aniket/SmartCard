from python-flask-server.openapi_server.services.user_service import *
import unittest
from openapi_server.models.user import User
from openapi_server.config_test import db
from openapi_server.user_service import UserService

class TestUserService(unittest.TestCase):

    def test_create_user(self):
        # Test creating user
        user = UserService.create_user("test_user", "test_password")
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.password, "test_password")

    def test_get_user_by_username(self):
        # Test getting user by username
        user = UserService.create_user("test_user", "test_password")
        retrieved_user = UserService.get_user_by_username("test_user")
        self.assertEqual(user.username, retrieved_user.username)
        self.assertEqual(user.password, retrieved_user.password)

    def test_get_user_by_username_nonexistent(self):
        # Test getting nonexistent user by username
        retrieved_user = UserService.get_user_by_username("nonexistent_user")
        self.assertIsNone(retrieved_user)

    def test_create_duplicate_user(self):
        # Test creating duplicate user
        UserService.create_user("test_user", "test_password")
        with self.assertRaises(Exception):
            UserService.create_user("test_user", "test_password")