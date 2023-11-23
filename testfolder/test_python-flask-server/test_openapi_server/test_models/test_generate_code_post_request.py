from python-flask-server.openapi_server.models.generate_code_post_request import *
import unittest
from openapi_server import db, GenerateCodePostRequestSchema, GenerateCodePostRequest

class TestGenerateCodePostRequest(unittest.TestCase):

    def setUp(self):
        self.db = db
        self.generate_code_post_request_schema = GenerateCodePostRequestSchema()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_generate_code_post_request_model(self):
        generate_code_post_request = GenerateCodePostRequest(language="python", open_api_url="https://example.com/api")
        db.session.add(generate_code_post_request)
        db.session.commit()

        self.assertEqual(generate_code_post_request.language, "python")
        self.assertEqual(generate_code_post_request.open_api_url, "https://example.com/api")

    def test_generate_code_post_request_serialization(self):
        generate_code_post_request = GenerateCodePostRequest(language="python", open_api_url="https://example.com/api")
        serialized_data = self.generate_code_post_request_schema.dump(generate_code_post_request)

        self.assertEqual(serialized_data["language"], "python")
        self.assertEqual(serialized_data["open_api_url"], "https://example.com/api")

    def test_generate_code_post_request_deserialization(self):
        data = {"language": "python", "open_api_url": "https://example.com/api"}
        deserialized_data = self.generate_code_post_request_schema.load(data)

        self.assertIsInstance(deserialized_data, GenerateCodePostRequest)
        self.assertEqual(deserialized_data.language, "python")
        self.assertEqual(deserialized_data.open_api_url, "https://example.com/api")

if __name__ == '__main__':
    unittest.main()