from python-flask-server.openapi_server.services.user_service import *
import unittest
from openapi_server.models.user import User
from openapi_server.config_test import db
import logging

logging.basicConfig(level=logging.INFO)

class TestUserService(unittest.TestCase):
    def test_create_user(self):
        logging.info(f"Testing create_user method.")
        # Test creating user with valid username and password
        user1 = UserService.create_user("test_user1", "password1")
        self.assertIsInstance(user1, User)
        self.assertEqual(user1.username, "test_user1")
        self.assertEqual(user1.password, "password1")

        # Test creating user with invalid username
        with self.assertRaises(ValueError):
            UserService.create_user("", "password2")

        # Test creating user with invalid password
        with self.assertRaises(ValueError):
            UserService.create_user("test_user2", "")

    def test_get_user_by_username(self):
        logging.info(f"Testing get_user_by_username method.")
        # Test getting user with valid username
        user1 = UserService.create_user("test_user3", "password3")
        user2 = UserService.get_user_by_username("test_user3")
        self.assertIsInstance(user2, User)
        self.assertEqual(user2.username, "test_user3")
        self.assertEqual(user2.password, "password3")

        # Test getting user with invalid username
        user3 = UserService.get_user_by_username("invalid_user")
        self.assertIsNone(user3)

if __name__ == '__main__':
    unittest.main()