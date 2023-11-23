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
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.password, "test_password")

    def test_get_user_by_username(self):
        user = UserService.create_user("test_user", "test_password")
        retrieved_user = UserService.get_user_by_username("test_user")
        self.assertEqual(user, retrieved_user)

    def test_get_user_by_nonexistent_username(self):
        user = UserService.create_user("test_user", "test_password")
        retrieved_user = UserService.get_user_by_username("nonexistent_user")
        self.assertIsNone(retrieved_user)

if __name__ == '__main__':
    unittest.main()