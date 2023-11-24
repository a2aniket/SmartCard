from python-flask-server.openapi_server.models.user import *
import unittest
from werkzeug.security import generate_password_hash, check_password_hash
from openapi_server.config_test import db, ma
from openapi_server.models.user import User, UserSchema

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User('test_user', 'test_password')
        self.db = db
        self.db.create_all()
        self.ma = ma
        self.ma.init_app(self.db)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_set_password(self):
        self.user.set_password('new_password')
        self.assertNotEqual(self.user.password, 'new_password')

    def test_check_password(self):
        self.assertTrue(self.user.check_password('test_password'))
        self.assertFalse(self.user.check_password('wrong_password'))

    def test_to_dict(self):
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['id'], None)
        self.assertEqual(user_dict['username'], 'test_user')

    def test_user_schema(self):
        user_schema = UserSchema()
        user_json = user_schema.dump(self.user)
        self.assertEqual(user_json['username'], 'test_user')
        self.assertEqual(user_json['password'], None)

if __name__ == '__main__':
    unittest.main()