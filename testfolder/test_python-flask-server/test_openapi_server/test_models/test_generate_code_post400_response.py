from python-flask-server.openapi_server.models.generate_code_post400_response import *
import unittest
from datetime import date, datetime
from openapi_server.config_test import db, ma
from openapi_server.models.generate_code_post400_response import GenerateCodePost400Response, GenerateCodePost400ResponseSchema

class TestGenerateCodePost400Response(unittest.TestCase):
    
    def setUp(self):
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
    def test_generate_code_post400_response(self):
        response = GenerateCodePost400Response(message="Bad Request")
        db.session.add(response)
        db.session.commit()
        
        result = GenerateCodePost400Response.query.filter_by(message="Bad Request").first()
        self.assertEqual(result, response)
        
    def test_generate_code_post400_response_schema(self):
        response = GenerateCodePost400Response(message="Bad Request")
        
        schema = GenerateCodePost400ResponseSchema()
        dump_data = schema.dump(response)
        load_data = schema.load(dump_data)
        
        self.assertEqual(load_data, response)
        
if __name__ == '__main__':
    unittest.main()