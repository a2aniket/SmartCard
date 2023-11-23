from python-flask-server.openapi_server.models.user import *
import unittest
from werkzeug.security import generate_password_hash, check_password_hash
from openapi_server.config_test import db,ma
from openapi_server.models.user import User, UserSchema

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.db = db
        self.db.create_all()
        self.user = User(username='test_user', password='test_password')
        self.db.session.add(self.user)
        self.db.session.commit()
        self.user_schema = UserSchema()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_set_password(self):
        self.user.set_password('new_password')
        self.assertTrue(check_password_hash(self.user.password, 'new_password'))

    def test_check_password(self):
        self.assertTrue(self.user.check_password('test_password'))
        self.assertFalse(self.user.check_password('wrong_password'))

    def test_to_dict(self):
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['id'], self.user.id)
        self.assertEqual(user_dict['username'], self.user.username)

    def test_user_schema(self):
        user_data = {
            'username': 'new_user',
            'password': 'new_password'
        }
        user = self.user_schema.load(user_data, session=self.db.session)
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, user_data['username'])
        self.assertTrue(check_password_hash(user.password, user_data['password']))