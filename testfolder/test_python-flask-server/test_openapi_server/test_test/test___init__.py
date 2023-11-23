from python-flask-server.openapi_server.test.__init__ import *
import unittest
import logging
import connexion
from flask_testing import TestCase
from openapi_server.encoder import JSONEncoder

class TestBaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = connexion.App(__name__, specification_dir='../openapi/')
        self.app.app.json_encoder = JSONEncoder
        self.app.add_api('openapi.yaml', pythonic_params=True)
        self.client = self.app.app.test_client()

    def test_create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = self.app.app
        self.assertIsNotNone(app)
        self.assertIsNotNone(app.json_encoder)
        self.assertIsNotNone(self.client)

    def test_create_app_with_invalid_spec_dir(self):
        with self.assertRaises(connexion.exceptions.SpecificationNotFound):
            app = connexion.App(__name__, specification_dir='../invalid_dir/')
            app.app.json_encoder = JSONEncoder
            app.add_api('openapi.yaml', pythonic_params=True)

if __name__ == '__main__':
    unittest.main()