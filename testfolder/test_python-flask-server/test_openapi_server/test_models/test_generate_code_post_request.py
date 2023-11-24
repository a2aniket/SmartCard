from python-flask-server.openapi_server.models.generate_code_post_request import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db, ma
from openapi_server.models.generate_code_post_request import GenerateCodePostRequest, GenerateCodePostRequestSchema

class TestGenerateCodePostRequest(unittest.TestCase):

    def setUp(self):
        self.generate_code_post_request = GenerateCodePostRequest(language='Python', open_api_url='https://example.com/api')
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_generate_code_post_request_language(self):
        self.assertEqual(self.generate_code_post_request.language, 'Python')

    def test_generate_code_post_request_open_api_url(self):
        self.assertEqual(self.generate_code_post_request.open_api_url, 'https://example.com/api')

    def test_generate_code_post_request_schema(self):
        data = {
            'language': 'Python',
            'open_api_url': 'https://example.com/api'
        }
        loaded_data = GenerateCodePostRequest_schema.load(data)
        self.assertEqual(loaded_data.language, 'Python')
        self.assertEqual(loaded_data.open_api_url, 'https://example.com/api')

if __name__ == '__main__':
    unittest.main()