from python-flask-server.openapi_server.models.user import *
import unittest
from werkzeug.security import generate_password_hash, check_password_hash
from openapi_server.config_test import db,ma
from openapi_server.models.user import User, UserSchema

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User('testUser', 'testPass')

    def test_set_password(self):
        self.assertIsNotNone(self.user.password)
        self.assertNotEqual(self.user.password, 'testPass')

    def test_check_password(self):
        self.assertTrue(self.user.check_password('testPass'))
        self.assertFalse(self.user.check_password('wrongPass'))

    def test_to_dict(self):
        expected_dict = {'id': self.user.id, 'username': 'testUser'}
        self.assertEqual(self.user.to_dict(), expected_dict)

    def test_UserSchema(self):
        user_schema = UserSchema()
        loaded_user = user_schema.load({'username': 'testUser', 'password': 'testPass'})
        self.assertIsInstance(loaded_user, User)
        self.assertEqual(loaded_user.username, 'testUser')
        self.assertIsNotNone(loaded_user.password)

if __name__ == '__main__':
    unittest.main()