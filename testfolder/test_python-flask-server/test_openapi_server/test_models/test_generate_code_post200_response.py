from python-flask-server.openapi_server.models.generate_code_post200_response import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db
from openapi_server.models import GenerateCodePost200Response, GenerateCodePost200ResponseSchema

class TestGenerateCodePost200Response(unittest.TestCase):

    def test_message_not_null(self):
        """Test that message is not null"""
        response = GenerateCodePost200Response(message="test message")
        self.assertIsNotNone(response.message)

    def test_message_type(self):
        """Test that message is of string type"""
        response = GenerateCodePost200Response(message="test message")
        self.assertIsInstance(response.message, str)

    def test_response_schema(self):
        """Test that response schema is working"""
        response = GenerateCodePost200Response(message="test message")
        serialized_response = GenerateCodePost200ResponseSchema().dump(response)
        self.assertIsInstance(serialized_response, dict)

    def test_responses_schema(self):
        """Test that responses schema is working"""
        responses = [GenerateCodePost200Response(message="test message1"),
                     GenerateCodePost200Response(message="test message2")]
        serialized_responses = GenerateCodePost200ResponseSchema(many=True).dump(responses)
        self.assertIsInstance(serialized_responses, list)
        self.assertEqual(len(serialized_responses), 2)

if __name__ == '__main__':
    unittest.main()