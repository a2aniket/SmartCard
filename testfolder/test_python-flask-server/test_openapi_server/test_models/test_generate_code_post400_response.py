from python-flask-server.openapi_server.models.generate_code_post400_response import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db, ma
from openapi_server.models.generate_code_post400_response import GenerateCodePost400Response, GenerateCodePost400ResponseSchema

class TestGenerateCodePost400Response(unittest.TestCase):

    def test_generate_code_post400_response_message(self):
        # Test if message is None
        response = GenerateCodePost400Response(message=None)
        self.assertIsNone(response.message)

        # Test if message is not None
        response = GenerateCodePost400Response(message="Bad Request")
        self.assertEqual(response.message, "Bad Request")

    def test_generate_code_post400_response_schema(self):
        # Test if schema is correctly loaded
        schema = GenerateCodePost400ResponseSchema()
        self.assertIsNotNone(schema)

    def test_generate_code_post400_response_serialize(self):
        # Test if serialization works correctly
        response = GenerateCodePost400Response(message="Bad Request")
        schema = GenerateCodePost400ResponseSchema()
        serialized = schema.dump(response)
        self.assertEqual(serialized["message"], "Bad Request")

    def test_generate_code_post400_response_deserialize(self):
        # Test if deserialization works correctly
        serialized = {"message": "Bad Request"}
        schema = GenerateCodePost400ResponseSchema()
        deserialized = schema.load(serialized)
        self.assertEqual(deserialized.message, "Bad Request")

if __name__ == '__main__':
    unittest.main()