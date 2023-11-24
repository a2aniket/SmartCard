from python-flask-server.openapi_server.services.user_service import *
import unittest
from openapi_server.models.user import User
from openapi_server.config_test import db
import logging
from openapi_server.services.user_service import UserService

logging.basicConfig(level=logging.INFO)

class TestUserService(unittest.TestCase):

    def setUp(self):
        db.create_all()
        self.user1 = User(username="test1", password="test1")
        db.session.add(self.user1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_user(self):
        user2 = UserService.create_user("test2", "test2")
        self.assertIsInstance(user2, User)
        self.assertEqual(user2.username, "test2")
        self.assertEqual(user2.password, "test2")

    def test_get_user_by_username(self):
        user = UserService.get_user_by_username("test1")
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, "test1")
        self.assertEqual(user.password, "test1")

    def test_create_user_with_same_username(self):
        with self.assertRaises(Exception):
            UserService.create_user("test1", "test1")

    def test_get_user_by_nonexistent_username(self):
        user = UserService.get_user_by_username("nonexistent")
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()