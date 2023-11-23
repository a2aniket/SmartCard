from python-flask-server.openapi_server.models.generate_code_post400_response import *
import unittest

class TestGenerateCodePost400Response(unittest.TestCase):
    
    def test_message_not_null(self):
        response = GenerateCodePost400Response(message="Bad Request")
        self.assertIsNotNone(response.message)
    
    def test_message_type(self):
        response = GenerateCodePost400Response(message="Bad Request")
        self.assertIsInstance(response.message, str)
    
    def test_serialization(self):
        response = GenerateCodePost400Response(message="Bad Request")
        serialized = GenerateCodePost400Response_schema.dump(response)
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized['message'], "Bad Request")
        
    def test_deserialization(self):
        serialized = {'message': 'Bad Request'}
        response = GenerateCodePost400Response_schema.load(serialized)
        self.assertIsInstance(response, GenerateCodePost400Response)
        self.assertEqual(response.message, "Bad Request")