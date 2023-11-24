from python-flask-server.openapi_server.test.__init__ import *
import logging
import unittest
import connexion
from flask_testing import TestCase
from openapi_server.encoder import JSONEncoder

class TestBaseCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../openapi/')
        app.app.json_encoder = JSONEncoder
        app.add_api('openapi.yaml', pythonic_params=True)
        return app.app

    def test_logger_level(self):
        self.assertEqual(logging.getLogger('connexion.operation').getEffectiveLevel(), logging.ERROR)

    def test_app_json_encoder(self):
        app = self.create_app()
        self.assertIsInstance(app.json_encoder, JSONEncoder)

    def test_api_pythonic_params(self):
        app = self.create_app()
        self.assertTrue(app.config['PYTHONIC_PARAMS'])

    def test_add_api(self):
        app = self.create_app()
        self.assertIsNotNone(app.url_map)

    def test_create_app(self):
        app = self.create_app()
        self.assertIsNotNone(app)

if __name__ == '__main__':
    unittest.main()