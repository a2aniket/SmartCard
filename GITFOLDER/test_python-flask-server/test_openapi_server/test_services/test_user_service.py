from python-flask-server.openapi_server.services.user_service import *
import unittest
from openapi_server.models.user import User
from openapi_server.config_test import db
import logging

logging.basicConfig(level=logging.INFO)

class TestUserService(unittest.TestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_user(self):
        user = UserService.create_user("testuser", "testpassword")
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.password, "testpassword")

    def test_get_user_by_username(self):
        user = UserService.create_user("testuser", "testpassword")
        retrieved_user = UserService.get_user_by_username("testuser")
        self.assertIsInstance(retrieved_user, User)
        self.assertEqual(user.id, retrieved_user.id)
        self.assertEqual(user.username, retrieved_user.username)
        self.assertEqual(user.password, retrieved_user.password)

    def test_get_user_by_nonexistent_username(self):
        retrieved_user = UserService.get_user_by_username("nonexistentuser")
        self.assertIsNone(retrieved_user)

if __name__ == "__main__":
    unittest.main()