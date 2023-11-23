from python-flask-server.openapi_server.models.generate_code_post400_response import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db, ma
from openapi_server.models.GenerateCodePost400Response import GenerateCodePost400Response, GenerateCodePost400ResponseSchema

class TestGenerateCodePost400Response(unittest.TestCase):

    def setUp(self):
        self.db = db
        self.db.drop_all()
        self.db.create_all()
        self.GenerateCodePost400Response = GenerateCodePost400Response
        self.GenerateCodePost400ResponseSchema = GenerateCodePost400ResponseSchema

    def test_GenerateCodePost400Response_model(self):
        response = self.GenerateCodePost400Response(message="Error: Bad Request")
        self.assertEqual(response.message, "Error: Bad Request")

    def test_GenerateCodePost400Response_schema(self):
        response_data = {"message": "Error: Bad Request"}
        response = self.GenerateCodePost400ResponseSchema().load(response_data)
        self.assertEqual(response.message, "Error: Bad Request")

    def test_GenerateCodePost400Response_schema_dump(self):
        response = self.GenerateCodePost400Response(message="Error: Bad Request")
        response_data = self.GenerateCodePost400ResponseSchema().dump(response)
        self.assertEqual(response_data["message"], "Error: Bad Request")

if __name__ == '__main__':
    unittest.main()