from python-flask-server.openapi_server.models.user import *
import unittest
from werkzeug.security import generate_password_hash, check_password_hash
from openapi_server.config_test import db,ma
from openapi_server.models.user import User, UserSchema

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user1 = User('test_user1', 'test_password1')
        self.user2 = User('test_user2', 'test_password2')
        db.session.add(self.user1)
        db.session.add(self.user2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_set_password(self):
        password = 'test_password'
        self.user1.set_password(password)
        self.assertTrue(check_password_hash(self.user1.password, password))

    def test_check_password(self):
        password = 'test_password'
        self.user1.set_password(password)
        self.assertTrue(self.user1.check_password(password))
        self.assertFalse(self.user1.check_password('wrong_password'))

    def test_to_dict(self):
        user_dict = self.user1.to_dict()
        self.assertEqual(user_dict['id'], self.user1.id)
        self.assertEqual(user_dict['username'], self.user1.username)

    def test_user_schema(self):
        user_schema = UserSchema()
        user_dict = user_schema.dump(self.user1)
        self.assertEqual(user_dict['id'], self.user1.id)
        self.assertEqual(user_dict['username'], self.user1.username)