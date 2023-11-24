from python-flask-server.openapi_server.models.user import *
import unittest
from werkzeug.security import generate_password_hash, check_password_hash
from openapi_server.config_test import db,ma
from openapi_server.models import User, UserSchema

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User('test_user', 'test_password')
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.delete(self.user)
        db.session.commit()

    def test_set_password(self):
        password = 'test_password'
        self.user.set_password(password)
        self.assertTrue(check_password_hash(self.user.password, password))

    def test_check_password(self):
        self.assertTrue(self.user.check_password('test_password'))
        self.assertFalse(self.user.check_password('wrong_password'))

    def test_to_dict(self):
        expected_dict = {'id': self.user.id, 'username': 'test_user'}
        self.assertDictEqual(self.user.to_dict(), expected_dict)

    def test_user_schema(self):
        user_dict = {'username': 'test_user', 'password': 'test_password'}
        schema = UserSchema()
        user = schema.load(user_dict, session=db.session)
        self.assertEqual(user.username, 'test_user')
        self.assertTrue(check_password_hash(user.password, 'test_password'))