import unittest
from openapi_server.services.user_service import UserService
from openapi_server.config_test import app, db

class TestUserService(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_user(self):
        # Test creating a new user with valid username and password
        user = UserService.create_user('test_user', 'test_password')
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.password, 'test_password')

    def test_get_user_by_username(self):
        # Test getting an existing user by username
        user = UserService.create_user('test_user', 'test_password')
        retrieved_user = UserService.get_user_by_username('test_user')
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.username, 'test_user')
        self.assertEqual(retrieved_user.password, 'test_password')

        # Test getting a non-existent user by username
        retrieved_user = UserService.get_user_by_username('non_existent_user')
        self.assertIsNone(retrieved_user)

if __name__ == '__main__':
    unittest.main()
```

Function `setUp` is used to set up the testing environment before running each test case. The function `tearDown` is used to clean up the environment after each test case. 

`test_create_user` function tests the `create_user` function of the `UserService` class. It creates a new user with valid username and password and checks if the user object is not None and the username and password are correct.

`test_get_user_by_username` function tests the `get_user_by_username` function of the `UserService` class. It creates a new user and retrieves it using the `get_user_by_username` function. It also tests if the function returns None when the username does not exist.