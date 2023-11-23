from python-flask-server.openapi_server.services.user_service import *
import unittest
from openapi_server.models.user import User
from openapi_server.config_test import db
from openapi_server.services.user_service import UserService

class TestUserService(unittest.TestCase):

    def test_create_user(self):
        user = UserService.create_user("test_user", "test_password")
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.password, "test_password")

    def test_get_user_by_username(self):
        user = UserService.create_user("test_user", "test_password")
        retrieved_user = UserService.get_user_by_username("test_user")
        self.assertIsInstance(retrieved_user, User)
        self.assertEqual(retrieved_user.username, "test_user")
        self.assertEqual(retrieved_user.password, "test_password")

    def test_get_user_by_nonexistent_username(self):
        retrieved_user = UserService.get_user_by_username("nonexistent_user")
        self.assertIsNone(retrieved_user)

    def test_create_user_with_empty_username(self):
        with self.assertRaises(ValueError):
            UserService.create_user("", "test_password")

    def test_create_user_with_empty_password(self):
        with self.assertRaises(ValueError):
            UserService.create_user("test_user", "")

    def test_create_duplicate_user(self):
        UserService.create_user("test_user", "test_password")
        with self.assertRaises(Exception):
            UserService.create_user("test_user", "test_password")

if __name__ == '__main__':
    unittest.main()