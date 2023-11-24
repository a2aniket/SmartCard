from python-flask-server.openapi_server.models.generate_code_post200_response import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db, ma, app
from openapi_server.models.generate_code_post200_response import GenerateCodePost200Response, GenerateCodePost200ResponseSchema

class TestGenerateCodePost200Response(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_GenerateCodePost200Response(self):
        # Test case to check if the GenerateCodePost200Response object is created successfully
        response = GenerateCodePost200Response(message="Test Message")
        self.assertIsInstance(response, GenerateCodePost200Response)

    def test_GenerateCodePost200ResponseSchema(self):
        # Test case to check if the GenerateCodePost200ResponseSchema object is created successfully
        response = GenerateCodePost200ResponseSchema()
        self.assertIsInstance(response, GenerateCodePost200ResponseSchema)

    def test_GenerateCodePost200ResponseSchema_serialization(self):
        # Test case to check if the serialization of GenerateCodePost200ResponseSchema object is correct
        response = GenerateCodePost200Response(message="Test Message")
        serialized_response = GenerateCodePost200Response_schema.dump(response)
        expected_response = {'message': 'Test Message'}
        self.assertEqual(serialized_response, expected_response)

    def test_GenerateCodePost200ResponseSchema_deserialization(self):
        # Test case to check if the deserialization of GenerateCodePost200ResponseSchema object is correct
        data = {'message': 'Test Message'}
        response = GenerateCodePost200Response_schema.load(data)
        expected_response = GenerateCodePost200Response(message="Test Message")
        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()