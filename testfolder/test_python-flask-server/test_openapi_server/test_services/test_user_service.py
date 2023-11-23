from python-flask-server.openapi_server.services.user_service import *
import unittest
from openapi_server.models.user import User
from openapi_server.config_test import db
from openapi_server.services.user_service import UserService

class TestUserService(unittest.TestCase):
    
    def setUp(self):
        """Setup a user for testing"""
        self.user = UserService.create_user("test_user", "test_password")

    def tearDown(self):
        """Remove the user from the database after testing"""
        db.session.delete(self.user)
        db.session.commit()

    def test_create_user(self):
        """Test creating a user"""
        user = UserService.create_user("new_user", "new_password")
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, "new_user")
        self.assertEqual(user.password, "new_password")
        db.session.delete(user)
        db.session.commit()

    def test_get_user_by_username(self):
        """Test getting a user by username"""
        user = UserService.get_user_by_username("test_user")
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.password, "test_password")

    def test_get_user_by_username_none(self):
        """Test getting a user by non-existent username"""
        user = UserService.get_user_by_username("fake_user")
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()