from python-flask-server.openapi_server.models.generate_code_post400_response import *
# Unit Test Cases for GenerateCodePost400Response Class and Schema

import unittest
from datetime import date, datetime
from openapi_server.config_test import db
from openapi_server.models.GenerateCodePost400Response import GenerateCodePost400Response, GenerateCodePost400ResponseSchema

class GenerateCodePost400ResponseTestCase(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # Test case to check if the GenerateCodePost400Response class has correct attributes
    def test_GenerateCodePost400Response_attributes(self):
        response = GenerateCodePost400Response(message="Bad Request")
        db.session.add(response)
        db.session.commit()
        self.assertEqual(response.message, "Bad Request")

    # Test case to check if the GenerateCodePost400ResponseSchema correctly serializes the response data
    def test_GenerateCodePost400ResponseSchema_serialization(self):
        response_data = {"message": "Bad Request"}
        response = GenerateCodePost400Response_schema.load(response_data)
        self.assertEqual(response.message, "Bad Request")
        serialized_data = GenerateCodePost400Response_schema.dump(response)
        self.assertEqual(serialized_data, response_data)

    # Test case to check if the GenerateCodePost400ResponseSchema correctly deserializes the response data
    def test_GenerateCodePost400ResponseSchema_deserialization(self):
        serialized_data = {"message": "Bad Request"}
        response = GenerateCodePost400Response_schema.load(serialized_data)
        self.assertEqual(response.message, "Bad Request")
        response_data = GenerateCodePost400Response_schema.dump(response)
        self.assertEqual(response_data, serialized_data)

if __name__ == '__main__':
    unittest.main()