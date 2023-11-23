from python-flask-server.openapi_server.models.generate_code_post200_response import *
import unittest
from datetime import date, datetime

from openapi_server.config_test import db, ma
from openapi_server.models.generate_code_post_200_response import GenerateCodePost200Response, GenerateCodePost200ResponseSchema

class TestGenerateCodePost200Response(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_generate_code_post_200_response_message(self):
        # Test if message is not null
        response = GenerateCodePost200Response(message='Test message')
        db.session.add(response)
        db.session.commit()
        self.assertIsNotNone(response.message)

    def test_generate_code_post_200_response_serialization(self):
        # Test if serialization works
        response = GenerateCodePost200Response(message='Test message')
        serialized = GenerateCodePost200Response_schema.dump(response)
        self.assertEqual(serialized['message'], 'Test message')

    def test_generate_code_post_200_responses_serialization(self):
        # Test if serialization of multiple responses works
        response1 = GenerateCodePost200Response(message='Test message 1')
        response2 = GenerateCodePost200Response(message='Test message 2')
        db.session.add_all([response1, response2])
        db.session.commit()
        serialized = GenerateCodePost200Responses_schema.dump([response1, response2])
        self.assertEqual(serialized[0]['message'], 'Test message 1')
        self.assertEqual(serialized[1]['message'], 'Test message 2')