from python-flask-server.openapi_server.models.generate_code_post_request import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db
from openapi_server.models import GenerateCodePostRequest, GenerateCodePostRequestSchema


class TestGenerateCodePostRequest(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_generate_code_post_request_model(self):
        test_model = GenerateCodePostRequest(language='python', open_api_url='http://localhost:8000/openapi.json')
        db.session.add(test_model)
        db.session.commit()

        result = GenerateCodePostRequest.query.filter_by(language='python').first()

        self.assertEqual(result.language, 'python')
        self.assertEqual(result.open_api_url, 'http://localhost:8000/openapi.json')

    def test_generate_code_post_request_schema_dump(self):
        test_model = GenerateCodePostRequest(language='python', open_api_url='http://localhost:8000/openapi.json')
        schema = GenerateCodePostRequestSchema()
        result = schema.dump(test_model)

        self.assertEqual(result['language'], 'python')
        self.assertEqual(result['open_api_url'], 'http://localhost:8000/openapi.json')

    def test_generate_code_post_request_schema_load(self):
        input_data = {
            'language': 'python',
            'open_api_url': 'http://localhost:8000/openapi.json'
        }
        schema = GenerateCodePostRequestSchema()
        result = schema.load(input_data)

        self.assertEqual(result.language, 'python')
        self.assertEqual(result.open_api_url, 'http://localhost:8000/openapi.json')

if __name__ == '__main__':
    unittest.main()