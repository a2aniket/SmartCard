from python-flask-server.openapi_server.services.user_service import *
import unittest
from unittest.mock import patch, MagicMock

from openapi_server.models.user import User
from openapi_server.config_test import db
from openapi_server.services.user_service import UserService


class TestUserService(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()

    def setUp(self):
        self.username = 'test_user'
        self.password = 'password'
        self.user = UserService.create_user(self.username, self.password)

    def tearDown(self):
        db.session.delete(self.user)
        db.session.commit()

    def test_create_user(self):
        username = 'test_user_2'
        password = 'password'
        user = UserService.create_user(username, password)
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, username)
        self.assertEqual(user.password, password)

    def test_get_user_by_username(self):
        username = 'test_user'
        user = UserService.get_user_by_username(username)
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, username)

    def test_get_user_by_username_not_found(self):
        username = 'non_existing_user'
        user = UserService.get_user_by_username(username)
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()