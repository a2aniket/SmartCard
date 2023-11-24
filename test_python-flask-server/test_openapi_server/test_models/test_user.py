from python-flask-server.openapi_server.models.user import *
import unittest
from werkzeug.security import generate_password_hash, check_password_hash
from openapi_server.config_test import db,ma
from openapi_server.models.user import User, UserSchema

class TestUser(unittest.TestCase):

    def test_user_creation(self):
        user = User('testuser', 'testpassword')
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(check_password_hash(user.password, 'testpassword'))

    def test_password_hashing(self):
        password = 'testpassword'
        hashed_password = generate_password_hash(password)
        self.assertTrue(check_password_hash(hashed_password, password))

    def test_user_to_dict(self):
        user = User('testuser', 'testpassword')
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['username'], 'testuser')

if __name__ == '__main__':
    unittest.main()