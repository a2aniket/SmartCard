from user import *
import unittest
from openapi_server.config_test import db, ma
from openapi_server.models import User, UserSchema
from werkzeug.security import generate_password_hash, check_password_hash

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(username='test_user', password='Test1234')
        db.session.add(self.user)
        db.session.commit()
        self.user_schema = UserSchema()

    def tearDown(self):
        db.session.delete(self.user)
        db.session.commit()

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'test_user')
        self.assertTrue(check_password_hash(self.user.password, 'Test1234'))

    def test_user_password_hashing(self):
        password = 'Test1234'
        hashed_password = generate_password_hash(password)
        self.assertNotEqual(password, hashed_password)

    def test_user_check_password(self):
        password = 'Test1234'
        hashed_password = generate_password_hash(password)
        self.assertTrue(check_password_hash(hashed_password, password))
        self.assertFalse(check_password_hash(hashed_password, 'test'))

    def test_user_to_dict(self):
        user_dict = self.user_schema.dump(self.user)
        self.assertEqual(user_dict['id'], self.user.id)
        self.assertEqual(user_dict['username'], self.user.username)

if __name__ == '__main__':
    unittest.main()