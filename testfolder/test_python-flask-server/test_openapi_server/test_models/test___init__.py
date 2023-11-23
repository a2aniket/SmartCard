from python-flask-server.openapi_server.models.__init__ import *
import unittest
from openapi_server.models.generate_code_post200_response import GenerateCodePost200Response
from openapi_server.models.generate_code_post400_response import GenerateCodePost400Response
from openapi_server.models.generate_code_post_request import GenerateCodePostRequest
from openapi_server.models.user import User
from openapi_server.config_test import db, app

class TestCodeGeneration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize the database
        with app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        # Delete all records from the database
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def setUp(self):
        # Add a user to the database
        with app.app_context():
            user = User(username="test_user", email="test_user@example.com")
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
        # Delete the user from the database
        with app.app_context():
            user = User.query.filter_by(username="test_user").first()
            db.session.delete(user)
            db.session.commit()

    def test_generate_code_with_valid_request(self):
        # Generate code with a valid request
        with app.test_client() as client:
            request_data = {
                "user_id": 1,
                "language": "python",
                "code": "print('Hello, world!')"
            }
            response = client.post("/generate_code", json=request_data)
            response_data = GenerateCodePost200Response.from_dict(response.json)
            # Ensure the response is successful
            self.assertEqual(response.status_code, 200)
            # Ensure the response contains the expected data
            self.assertIsNotNone(response_data)
            self.assertIsNotNone(response_data.generated_code)
            self.assertEqual(response_data.generated_code, "print('Hello, world!')")

    def test_generate_code_with_missing_user_id(self):
        # Generate code with a request missing the user_id parameter
        with app.test_client() as client:
            request_data = {
                "language": "python",
                "code": "print('Hello, world!')"
            }
            response = client.post("/generate_code", json=request_data)
            response_data = GenerateCodePost400Response.from_dict(response.json)
            # Ensure the response is a bad request
            self.assertEqual(response.status_code, 400)
            # Ensure the response contains the expected error message
            self.assertIsNotNone(response_data)
            self.assertIsNotNone(response_data.detail)
            self.assertEqual(response_data.detail, "user_id is a required property")

    def test_generate_code_with_invalid_user_id(self):
        # Generate code with a request containing an invalid user_id parameter
        with app.test_client() as client:
            request_data = {
                "user_id": "invalid",
                "language": "python",
                "code": "print('Hello, world!')"
            }
            response = client.post("/generate_code", json=request_data)
            response_data = GenerateCodePost400Response.from_dict(response.json)
            # Ensure the response is a bad request
            self.assertEqual(response.status_code, 400)
            # Ensure the response contains the expected error message
            self.assertIsNotNone(response_data)
            self.assertIsNotNone(response_data.detail)
            self.assertEqual(response_data.detail, "user_id should be integer")

    def test_generate_code_with_missing_language(self):
        # Generate code with a request missing the language parameter
        with app.test_client() as client:
            request_data = {
                "user_id": 1,
                "code": "print('Hello, world!')"
            }
            response = client.post("/generate_code", json=request_data)
            response_data = GenerateCodePost400Response.from_dict(response.json)
            # Ensure the response is a bad request
            self.assertEqual(response.status_code, 400)
            # Ensure the response contains the expected error message
            self.assertIsNotNone(response_data)
            self.assertIsNotNone(response_data.detail)
            self.assertEqual(response_data.detail, "language is a required property")

    def test_generate_code_with_invalid_language(self):
        # Generate code with a request containing an invalid language parameter
        with app.test_client() as client:
            request_data = {
                "user_id": 1,
                "language": "invalid",
                "code": "print('Hello, world!')"
            }
            response = client.post("/generate_code", json=request_data)
            response_data = GenerateCodePost400Response.from_dict(response.json)
            # Ensure the response is a bad request
            self.assertEqual(response.status_code, 400)
            # Ensure the response contains the expected error message
            self.assertIsNotNone(response_data)
            self.assertIsNotNone(response_data.detail)
            self.assertEqual(response_data.detail, "invalid is not one of ['python', 'java', 'c', 'cpp']")

    def test_generate_code_with_missing_code(self):
        # Generate code with a request missing the code parameter
        with app.test_client() as client:
            request_data = {
                "user_id": 1,
                "language": "python"
            }
            response = client.post("/generate_code", json=request_data)
            response_data = GenerateCodePost400Response.from_dict(response.json)
            # Ensure the response is a bad request
            self.assertEqual(response.status_code, 400)
            # Ensure the response contains the expected error message
            self.assertIsNotNone(response_data)
            self.assertIsNotNone(response_data.detail)
            self.assertEqual(response_data.detail, "code is a required property")