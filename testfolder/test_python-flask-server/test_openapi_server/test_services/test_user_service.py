from python-flask-server.openapi_server.services.user_service import *
import unittest
from openapi_server.models.user import User
from openapi_server.config_test import db
from openapi_server.services.user_service import UserService

class TestUserService(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_user(self):
        user = UserService.create_user("test_user", "test_password")
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.password, "test_password")

    def test_get_user_by_username(self):
        UserService.create_user("test_user", "test_password")
        user = UserService.get_user_by_username("test_user")
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.password, "test_password")

    def test_create_user_duplicate_username(self):
        UserService.create_user("test_user", "test_password")
        with self.assertRaises(Exception):
            UserService.create_user("test_user", "test_password2")

    def test_get_user_by_username_not_found(self):
        user = UserService.get_user_by_username("non_existent_user")
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()