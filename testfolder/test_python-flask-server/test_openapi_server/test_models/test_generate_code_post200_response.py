from python-flask-server.openapi_server.models.generate_code_post200_response import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db
from openapi_server.models.generate_code_post200_response import GenerateCodePost200Response, GenerateCodePost200ResponseSchema

class TestGenerateCodePost200Response(unittest.TestCase):

    def setUp(self):
        self.test_message = "Test message"
        self.test_response = GenerateCodePost200Response(message=self.test_message)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_generate_code_post200_response_model(self):
        self.assertIsInstance(self.test_response, GenerateCodePost200Response)
        self.assertEqual(self.test_response.message, self.test_message)

    def test_generate_code_post200_response_schema(self):
        serialized_response = GenerateCodePost200Response_schema.dump(self.test_response)
        self.assertIsInstance(serialized_response, dict)
        self.assertIn('message', serialized_response)
        self.assertEqual(serialized_response['message'], self.test_message)

    def test_generate_code_post200_responses_schema(self):
        test_response_list = [self.test_response]
        serialized_response_list = GenerateCodePost200Responses_schema.dump(test_response_list)
        self.assertIsInstance(serialized_response_list, list)
        self.assertEqual(len(serialized_response_list), 1)
        serialized_response = serialized_response_list[0]
        self.assertIsInstance(serialized_response, dict)
        self.assertIn('message', serialized_response)
        self.assertEqual(serialized_response['message'], self.test_message)