from python-flask-server.openapi_server.models.generate_code_post_request import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db, ma
from openapi_server.models.generate_code_post_request import GenerateCodePostRequest, GenerateCodePostRequestSchema

class TestGenerateCodePostRequest(unittest.TestCase):
    def setUp(self):
        self.request = GenerateCodePostRequest(language="python", open_api_url="https://example.com/openapi")

    def test_generate_code_post_request_language(self):
        self.assertEqual(self.request.language, "python")

    def test_generate_code_post_request_open_api_url(self):
        self.assertEqual(self.request.open_api_url, "https://example.com/openapi")

    def test_generate_code_post_request_table_name(self):
        self.assertEqual(GenerateCodePostRequest.__tablename__, "GenerateCodePostRequest")

    def test_generate_code_post_request_language_column(self):
        self.assertIsInstance(GenerateCodePostRequest.language, db.Column)

    def test_generate_code_post_request_open_api_url_column(self):
        self.assertIsInstance(GenerateCodePostRequest.open_api_url, db.Column)

    def test_generate_code_post_request_schema(self):
        self.assertIsInstance(GenerateCodePostRequest_schema, ma.SQLAlchemyAutoSchema)

    def test_generate_code_post_request_serialize(self):
        serialized_request = GenerateCodePostRequest_schema.dump(self.request)
        self.assertIsInstance(serialized_request, dict)

    def test_generate_code_post_request_deserialize(self):
        request_data = {"language": "python", "open_api_url": "https://example.com/openapi"}
        deserialized_request = GenerateCodePostRequest_schema.load(request_data)
        self.assertIsInstance(deserialized_request, GenerateCodePostRequest)

if __name__ == '__main__':
    unittest.main()