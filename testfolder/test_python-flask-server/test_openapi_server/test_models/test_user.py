from python-flask-server.openapi_server.models.user import *
import unittest
from werkzeug.security import generate_password_hash, check_password_hash
from openapi_server.config_test import db,ma
from openapi_server.models.user import User, UserSchema

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user1 = User(username="user1", password="password1")
        db.session.add(self.user1)
        db.session.commit()

    def test_set_password(self):
        self.user1.set_password("newpassword")
        self.assertTrue(check_password_hash(self.user1.password, "newpassword"))

    def test_check_password(self):
        self.assertTrue(self.user1.check_password("password1"))
        self.assertFalse(self.user1.check_password("wrongpassword"))

    def test_to_dict(self):
        user_dict = self.user1.to_dict()
        self.assertEqual(user_dict['id'], self.user1.id)
        self.assertEqual(user_dict['username'], self.user1.username)

    def test_user_schema(self):
        user_schema = UserSchema()
        user = user_schema.load({'username': 'user2', 'password': 'password2'})
        self.assertEqual(user.username, 'user2')
        self.assertEqual(check_password_hash(user.password, 'password2'), True)