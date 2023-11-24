from python-flask-server.openapi_server.services.user_service import *
import unittest
from openapi_server.models.user import User
from openapi_server.config_test import db
import logging

logging.basicConfig(level=logging.INFO)

class TestUserService(unittest.TestCase):
    def test_create_user(self):
        """
        Test creating a new user
        """
        user = UserService.create_user("testuser", "testpassword")
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.password, "testpassword")
        self.assertIsNotNone(user.id)

    def test_get_user_by_username(self):
        """
        Test getting user by username
        """
        user = UserService.create_user("testuser", "testpassword")
        retrieved_user = UserService.get_user_by_username("testuser")
        self.assertIsInstance(retrieved_user, User)
        self.assertEqual(retrieved_user.username, "testuser")
        self.assertEqual(retrieved_user.password, "testpassword")
        self.assertEqual(retrieved_user.id, user.id)

    def test_get_user_by_nonexistent_username(self):
        """
        Test getting a user by a nonexistent username
        """
        retrieved_user = UserService.get_user_by_username("nonexistentuser")
        self.assertIsNone(retrieved_user)

if __name__ == '__main__':
    unittest.main()