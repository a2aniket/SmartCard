from python-flask-server.openapi_server.models.generate_code_post_request import *
import unittest
from datetime import date, datetime

from openapi_server.config_test import db, ma
from openapi_server.models import GenerateCodePostRequest, GenerateCodePostRequestSchema


class TestGenerateCodePostRequest(unittest.TestCase):
    def setUp(self):
        db.create_all()

        self.request = GenerateCodePostRequest(language='Python', open_api_url='http://example.com/openapi')

        db.session.add(self.request)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_generate_code_post_request_model(self):
        self.assertEqual(self.request.language, 'Python')
        self.assertEqual(self.request.open_api_url, 'http://example.com/openapi')

    def test_generate_code_post_request_schema_dump(self):
        schema = GenerateCodePostRequestSchema()
        dump_data = schema.dump(self.request)

        self.assertEqual(dump_data['language'], 'Python')
        self.assertEqual(dump_data['open_api_url'], 'http://example.com/openapi')

    def test_generate_code_post_request_schema_load(self):
        data = {
            'language': 'Java',
            'open_api_url': 'http://example.com/openapi/v2'
        }

        schema = GenerateCodePostRequestSchema()
        request = schema.load(data)

        self.assertEqual(request.language, 'Java')
        self.assertEqual(request.open_api_url, 'http://example.com/openapi/v2')

    def test_generate_code_post_request_schema_load_multiple(self):
        data = [
            {
                'language': 'Ruby',
                'open_api_url': 'http://example.com/openapi/v3'
            },
            {
                'language': 'PHP',
                'open_api_url': 'http://example.com/openapi/v4'
            }
        ]

        schema = GenerateCodePostRequestSchema(many=True)
        requests = schema.load(data)

        self.assertEqual(len(requests), 2)
        self.assertEqual(requests[0].language, 'Ruby')
        self.assertEqual(requests[0].open_api_url, 'http://example.com/openapi/v3')
        self.assertEqual(requests[1].language, 'PHP')
        self.assertEqual(requests[1].open_api_url, 'http://example.com/openapi/v4')