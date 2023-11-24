from python-flask-server.openapi_server.models.generate_code_post400_response import *
import unittest

class TestGenerateCodePost400Response(unittest.TestCase):
    
    def test_message_not_null(self):
        response = GenerateCodePost400Response(message=None)
        self.assertIsNone(response.message)
        
    def test_message_type(self):
        response = GenerateCodePost400Response(message="test")
        self.assertIsInstance(response.message, str)
        
    def test_schema_serialization(self):
        response = GenerateCodePost400Response(message="test")
        serialized = GenerateCodePost400Response_schema.dump(response)
        self.assertEqual(serialized["message"], "test")
        
    def test_schema_deserialization(self):
        data = {"message": "test"}
        deserialized = GenerateCodePost400Response_schema.load(data)
        self.assertEqual(deserialized.message, "test")