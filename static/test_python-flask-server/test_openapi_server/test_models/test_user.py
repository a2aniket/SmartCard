from python-flask-server.openapi_server.models.user import *
import unittest
from werkzeug.security import generate_password_hash, check_password_hash
from openapi_server.config_test import db,ma
from openapi_server.models.user import User, UserSchema

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.user = User('test_user', 'test_password')
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.delete(self.user)
        db.session.commit()

    def test_user_init(self):
        self.assertEqual(self.user.username, 'test_user')
        self.assertTrue(check_password_hash(self.user.password, 'test_password'))

    def test_user_set_password(self):
        self.user.set_password('new_password')
        self.assertTrue(check_password_hash(self.user.password, 'new_password'))

    def test_user_check_password(self):
        self.assertTrue(self.user.check_password('test_password'))
        self.assertFalse(self.user.check_password('wrong_password'))

    def test_user_to_dict(self):
        expected_dict = {
            'id': self.user.id,
            'username': 'test_user',
        }
        self.assertEqual(self.user.to_dict(), expected_dict)

    def test_user_schema(self):
        user_schema = UserSchema()
        result = user_schema.dump(self.user)
        expected_dict = {
            'id': self.user.id,
            'username': 'test_user',
        }
        self.assertEqual(result, expected_dict)