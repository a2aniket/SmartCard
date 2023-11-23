from python-flask-server.openapi_server.models.generate_code_post200_response import *
import unittest
from datetime import date, datetime  
from openapi_server.config_test import db, ma
from openapi_server.models.generate_code_post200_response import GenerateCodePost200Response, GenerateCodePost200ResponseSchema

class TestGenerateCodePost200Response(unittest.TestCase):
    
    def setUp(self):
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
    def test_GenerateCodePost200Response(self):
        response = GenerateCodePost200Response(message="Test Message")
        db.session.add(response)
        db.session.commit()
        self.assertEqual(response.message, "Test Message")
        
    def test_GenerateCodePost200ResponseSchema_serialization(self):
        response = GenerateCodePost200Response(message="Test Message")
        serialized = GenerateCodePost200Response_schema.dump(response)
        expected = {'message': 'Test Message'}
        self.assertEqual(serialized, expected)
        
    def test_GenerateCodePost200ResponseSchema_deserialization(self):
        data = {'message': 'Test Message'}
        deserialized = GenerateCodePost200Response_schema.load(data)
        expected = GenerateCodePost200Response(message="Test Message")
        self.assertEqual(deserialized, expected)
        
    def test_GenerateCodePost200ResponsesSchema_serialization(self):
        responses = [GenerateCodePost200Response(message="Test Message 1"), GenerateCodePost200Response(message="Test Message 2")]
        serialized = GenerateCodePost200Responses_schema.dump(responses)
        expected = [{'message': 'Test Message 1'}, {'message': 'Test Message 2'}]
        self.assertEqual(serialized, expected)
        
    def test_GenerateCodePost200ResponsesSchema_deserialization(self):
        data = [{'message': 'Test Message 1'}, {'message': 'Test Message 2'}]
        deserialized = GenerateCodePost200Responses_schema.load(data, many=True)
        expected = [GenerateCodePost200Response(message="Test Message 1"), GenerateCodePost200Response(message="Test Message 2")]
        self.assertEqual(deserialized, expected)