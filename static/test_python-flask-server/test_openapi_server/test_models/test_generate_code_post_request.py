from python-flask-server.openapi_server.models.generate_code_post_request import *
import unittest
from openapi_server.config_test import db
from openapi_server.models.generate_code_post_request import GenerateCodePostRequest, GenerateCodePostRequestSchema

class TestGenerateCodePostRequest(unittest.TestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_generate_code_post_request(self):
        language = "Python"
        open_api_url = "http://example.com/openapi"
        # create GenerateCodePostRequest object
        generate_code_post_request = GenerateCodePostRequest(language=language, open_api_url=open_api_url)
        # add GenerateCodePostRequest to database
        db.session.add(generate_code_post_request)
        db.session.commit()
        # get GenerateCodePostRequest object from database
        result = GenerateCodePostRequest.query.filter_by(language=language).first()
        # assert that generated and retrieved GenerateCodePostRequest objects are equal
        self.assertEqual(generate_code_post_request, result)

    def test_generate_code_post_request_schema(self):
        language = "Python"
        open_api_url = "http://example.com/openapi"
        # create GenerateCodePostRequest object
        generate_code_post_request = GenerateCodePostRequest(language=language, open_api_url=open_api_url)
        # serialize GenerateCodePostRequest object
        generate_code_post_request_data = GenerateCodePostRequestSchema().dump(generate_code_post_request)
        # assert that serialized data has correct fields and values
        self.assertEqual(generate_code_post_request_data["language"], language)
        self.assertEqual(generate_code_post_request_data["open_api_url"], open_api_url)

if __name__ == '__main__':
    unittest.main()