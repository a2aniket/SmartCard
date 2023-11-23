from python-flask-server.openapi_server.test.__init__ import *
import unittest
import logging
import connexion
from flask_testing import TestCase
from openapi_server.encoder import JSONEncoder

class TestBase(TestCase):
    
    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../openapi/')
        app.app.json_encoder = JSONEncoder
        app.add_api('openapi.yaml', pythonic_params=True)
        return app.app

    def test_create_app(self):
        self.assertIsNotNone(self.app)
        
    def test_logging_level(self):
        self.assertEqual(logging.getLogger('connexion.operation').getEffectiveLevel(), logging.ERROR)
        
    def test_json_encoder(self):
        self.assertIsInstance(self.app.json_encoder, JSONEncoder)
        
    def test_add_api(self):
        self.assertIsNotNone(self.app)
        self.assertIsNotNone(self.app.add_api('openapi.yaml', pythonic_params=True))
        
if __name__ == '__main__':
    unittest.main()