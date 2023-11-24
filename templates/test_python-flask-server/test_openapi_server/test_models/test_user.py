from python-flask-server.openapi_server.models.user import *
import unittest
from openapi_server import User, db, ma

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user1 = User(username='test_user_1', password='password1')
        self.user2 = User(username='test_user_2', password='password2')
        db.session.add(self.user1)
        db.session.add(self.user2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_set_password(self):
        self.user1.set_password('new_password')
        self.assertNotEqual(self.user1.password, 'new_password')

    def test_check_password(self):
        self.assertTrue(self.user1.check_password('password1'))
        self.assertFalse(self.user1.check_password('wrong_password'))

    def test_to_dict(self):
        self.assertEqual(self.user1.to_dict(), {'id': 1, 'username': 'test_user_1'})

    def test_user_schema(self):
        user_schema = UserSchema()
        user_dict = user_schema.dump(self.user1)
        self.assertEqual(user_dict, {'id': 1, 'username': 'test_user_1'})