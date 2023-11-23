from python-flask-server.openapi_server.models.generate_code_post400_response import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db, ma
from openapi_server.models.generate_code_post400_response import GenerateCodePost400Response, GenerateCodePost400ResponseSchema


class TestGenerateCodePost400Response(unittest.TestCase):

    def setUp(self):
        self.message = "Bad Request"
        self.response = GenerateCodePost400Response(message=self.message)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_generate_code_post400_response_model(self):
        self.assertIsInstance(self.response, GenerateCodePost400Response)
        self.assertEqual(self.response.message, self.message)

    def test_generate_code_post400_response_schema(self):
        self.assertIsInstance(GenerateCodePost400Response_schema, ma.SQLAlchemyAutoSchema)

    def test_generate_code_post400_response_serialize(self):
        serialized_response = GenerateCodePost400Response_schema.dump(self.response)
        self.assertIsInstance(serialized_response, dict)
        self.assertEqual(serialized_response['message'], self.message)

    def test_generate_code_post400_responses_schema(self):
        responses = [self.response, self.response]
        serialized_responses = GenerateCodePost400Responses_schema.dump(responses)
        self.assertIsInstance(serialized_responses, list)
        self.assertEqual(len(serialized_responses), 2)
        self.assertEqual(serialized_responses[0]['message'], self.message)
        self.assertEqual(serialized_responses[1]['message'], self.message)