from user_controller import *
import unittest
from openapi_server import app

class TestUserAPI(unittest.TestCase):

    def test_create_user(self):
        with app.test_client() as client:
            # Test create user with valid data
            response = client.post('/users', json={'username': 'testuser', 'password': 'testpassword'})
            self.assertEqual(response.status_code, 201)
            # Test create user with missing data
            response = client.post('/users', json={'username': 'testuser'})
            self.assertEqual(response.status_code, 400)

    def test_get_user_by_username(self):
        with app.test_client() as client:
            # Test get user with valid username
            response = client.get('/users/testuser')
            self.assertEqual(response.status_code, 200)
            # Test get user with invalid username
            response = client.get('/users/invaliduser')
            self.assertEqual(response.status_code, 404)
            
if __name__ == '__main__':
    unittest.main()