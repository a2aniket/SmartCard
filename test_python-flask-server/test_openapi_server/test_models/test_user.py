from python-flask-server.openapi_server.models.user import *
import unittest
from openapi_server.config_test import db, ma
from openapi_server.models import User, UserSchema
from werkzeug.security import check_password_hash


class TestUser(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_set_password(self):
        user = User(username='test', password='password')
        self.assertIsNotNone(user.password)

    def test_check_password(self):
        user = User(username='test', password='password')
        self.assertTrue(user.check_password('password'))
        self.assertFalse(user.check_password('notpassword'))

    def test_to_dict(self):
        user = User(username='test', password='password')
        user_dict = user.to_dict()
        self.assertEqual(user_dict['username'], 'test')
        self.assertEqual(user_dict['id'], None)

    def test_user_schema(self):
        user = User(username='test', password='password')
        user_dict = UserSchema().dump(user)
        self.assertEqual(user_dict['username'], 'test')
        self.assertEqual(user_dict['id'], None)

if __name__ == '__main__':
    unittest.main()