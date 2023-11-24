from python-flask-server.openapi_server.models.generate_code_post200_response import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db, ma
from openapi_server.models.generate_code_post200_response import GenerateCodePost200Response, GenerateCodePost200ResponseSchema

class TestGenerateCodePost200Response(unittest.TestCase):

    def setUp(self):
        self.message = "Test Message"
        self.response = GenerateCodePost200Response(message=self.message)
        db.session.add(self.response)
        db.session.commit()

    def tearDown(self):
        db.session.delete(self.response)
        db.session.commit()

    def test_generate_code_post200_response_model(self):
        self.assertEqual(self.response.message, self.message)

    def test_generate_code_post200_response_schema_dump(self):
        data = GenerateCodePost200Response_schema.dump(self.response)
        self.assertEqual(data['message'], self.message)

    def test_generate_code_post200_response_schema_load(self):
        data = {'message': self.message}
        response = GenerateCodePost200ResponseSchema().load(data)
        self.assertIsInstance(response, GenerateCodePost200Response)
        self.assertEqual(response.message, self.message)