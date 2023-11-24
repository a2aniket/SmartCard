from python-flask-server.openapi_server.models.generate_code_post_request import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db, ma
from openapi_server.models.generate_code_post_request import GenerateCodePostRequest, GenerateCodePostRequestSchema

class TestGenerateCodePostRequest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.db = db
        self.db.create_all()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_generate_code_post_request(self):
        # Test case for generating code post request

        # Create GenerateCodePostRequest object
        generate_code_post_request = GenerateCodePostRequest(
            language='Python',
            open_api_url='http://localhost:8080/swagger.json'
        )

        # Add GenerateCodePostRequest object to database session
        self.db.session.add(generate_code_post_request)

        # Commit session to database
        self.db.session.commit()

        # Query database for GenerateCodePostRequest object
        result = self.db.session.query(GenerateCodePostRequest).filter_by(language='Python').first()

        # Assert that GenerateCodePostRequest object was created and added to database
        self.assertIsNotNone(result)
        self.assertEqual(result.language, 'Python')
        self.assertEqual(result.open_api_url, 'http://localhost:8080/swagger.json')

    def test_generate_code_post_request_schema(self):
        # Test case for GenerateCodePostRequestSchema

        # Create GenerateCodePostRequest object
        generate_code_post_request = GenerateCodePostRequest(
            language='Python',
            open_api_url='http://localhost:8080/swagger.json'
        )

        # Dump GenerateCodePostRequest object to JSON using GenerateCodePostRequestSchema
        result = GenerateCodePostRequestSchema().dump(generate_code_post_request)

        # Assert that JSON output is correct
        self.assertEqual(result['language'], 'Python')
        self.assertEqual(result['open_api_url'], 'http://localhost:8080/swagger.json')

if __name__ == '__main__':
    unittest.main()