from python-flask-server.openapi_server.models.generate_code_post_request import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db, ma
from openapi_server.models import GenerateCodePostRequest, GenerateCodePostRequestSchema

class TestGenerateCodePostRequest(unittest.TestCase):
    
    def setUp(self):
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    def test_generate_code_post_request_model(self):
        '''
        Test if GenerateCodePostRequest model is created successfully
        '''
        request = GenerateCodePostRequest(language='Python', open_api_url='https://example.com')
        db.session.add(request)
        db.session.commit()
        self.assertEqual(request.language, 'Python')
        self.assertEqual(request.open_api_url, 'https://example.com')
    
    def test_generate_code_post_request_schema(self):
        '''
        Test if GenerateCodePostRequestSchema is able to serialize and deserialize GenerateCodePostRequest object
        '''
        request = GenerateCodePostRequest(language='Python', open_api_url='https://example.com')
        serialized_request = GenerateCodePostRequest_schema.dump(request)
        self.assertEqual(serialized_request['language'], 'Python')
        self.assertEqual(serialized_request['open_api_url'], 'https://example.com')
        deserialized_request = GenerateCodePostRequest_schema.load(serialized_request)
        self.assertIsInstance(deserialized_request, GenerateCodePostRequest)
        self.assertEqual(deserialized_request.language, 'Python')
        self.assertEqual(deserialized_request.open_api_url, 'https://example.com')