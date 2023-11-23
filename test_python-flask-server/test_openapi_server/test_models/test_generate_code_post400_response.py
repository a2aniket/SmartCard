from python-flask-server.openapi_server.models.generate_code_post400_response import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db, ma
from your_module import GenerateCodePost400Response, GenerateCodePost400ResponseSchema

class TestGenerateCodePost400Response(unittest.TestCase):
    
    def setUp(self):
        self.message = "Bad Request"
        self.response = GenerateCodePost400Response(message=self.message)
    
    def test_message_value(self):
        self.assertEqual(self.response.message, self.message)
    
    def test_message_type(self):
        self.assertIsInstance(self.response.message, str)
    
    def test_serialization(self):
        serialized = GenerateCodePost400Response_schema.dump(self.response)
        self.assertIsInstance(serialized, dict)
        self.assertIn("message", serialized)
        self.assertEqual(serialized["message"], self.message)

if __name__ == "__main__":
    unittest.main()