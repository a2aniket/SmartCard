from python-flask-server.openapi_server.models.generate_code_post200_response import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db, ma
from openapi_server.models.generate_code_post200_response import GenerateCodePost200Response, GenerateCodePost200ResponseSchema

class TestGenerateCodePost200Response(unittest.TestCase):

    def test_message_exists(self):
        response = GenerateCodePost200Response(message="Hello World")
        self.assertEqual(response.message, "Hello World")

    def test_message_not_null(self):
        response = GenerateCodePost200Response(message=None)
        self.assertIsNone(response.message)

    def test_message_type(self):
        response = GenerateCodePost200Response(message="Hello World")
        self.assertIsInstance(response.message, str)

    def test_schema_loads_instance(self):
        response = GenerateCodePost200Response(message="Hello World")
        serialized_data = GenerateCodePost200Response_schema.dump(response)
        deserialized_data = GenerateCodePost200Response_schema.load(serialized_data)
        self.assertIsInstance(deserialized_data, GenerateCodePost200Response)

    def test_schema_loads_multiple_instances(self):
        response1 = GenerateCodePost200Response(message="Hello World")
        response2 = GenerateCodePost200Response(message="Goodbye World")
        responses = [response1, response2]
        serialized_data = GenerateCodePost200Responses_schema.dump(responses)
        deserialized_data = GenerateCodePost200Responses_schema.load(serialized_data, many=True)
        self.assertIsInstance(deserialized_data, list)
        self.assertIsInstance(deserialized_data[0], GenerateCodePost200Response)
        self.assertIsInstance(deserialized_data[1], GenerateCodePost200Response)

if __name__ == '__main__':
    unittest.main()