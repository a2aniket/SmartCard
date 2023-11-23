from python-flask-server.openapi_server.services.user_service import *
import unittest
from openapi_server.models.user import User
from openapi_server.config_test import db
import logging

logging.basicConfig(level=logging.INFO)

class TestUserService(unittest.TestCase):

    def test_create_user(self):
        logging.info("Testing create_user function.")
        # Test for creating a user
        user = UserService.create_user("testuser", "testpassword")
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.password, "testpassword")

    def test_get_user_by_username(self):
        logging.info("Testing get_user_by_username function.")
        # Test for getting a user by username
        user = UserService.create_user("testuser", "testpassword")
        user_by_username = UserService.get_user_by_username("testuser")
        self.assertEqual(user, user_by_username)

    def test_get_nonexistent_user_by_username(self):
        logging.info("Testing get_user_by_username function for nonexistent user.")
        # Test for getting a nonexistent user by username
        user_by_username = UserService.get_user_by_username("nonexistentuser")
        self.assertIsNone(user_by_username)

if __name__ == '__main__':
    unittest.main()