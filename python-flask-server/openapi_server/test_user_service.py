from services.user_service import *
import unittest
from openapi_server.models.user import User
from openapi_server.config_test import db
import logging

logging.basicConfig(level=logging.INFO)

class TestUserService(unittest.TestCase):
    def test_create_user(self):
        logging.info("Testing create_user function.")
        username = "testuser"
        password = "testpassword"
        user = UserService.create_user(username, password)
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, username)
        self.assertEqual(user.password, password)

    def test_get_user_by_username(self):
        logging.info("Testing get_user_by_username function.")
        username = "testuser"
        password = "testpassword"
        UserService.create_user(username, password)
        user = UserService.get_user_by_username(username)
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, username)
        self.assertEqual(user.password, password)

    def test_get_user_by_username_not_exist(self):
        logging.info("Testing get_user_by_username function when user does not exist.")
        username = "nonexistinguser"
        user = UserService.get_user_by_username(username)
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()