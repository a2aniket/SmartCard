from python-flask-server.openapi_server.models.generate_code_post200_response import *
import unittest

class TestGenerateCodePost200Response(unittest.TestCase):

    def test_message_not_null(self):
        response = GenerateCodePost200Response(message="Test")
        self.assertIsNotNone(response.message)

    def test_message_type(self):
        response = GenerateCodePost200Response(message="Test")
        self.assertIsInstance(response.message, str)

    def test_Schema(self):
        response = GenerateCodePost200Response(message="Test")
        schema = GenerateCodePost200ResponseSchema()
        result = schema.dump(response)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn('message', result)