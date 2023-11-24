from python-flask-server.openapi_server.test.__init__ import *
import logging
import unittest
import connexion
from flask_testing import TestCase
from openapi_server.encoder import JSONEncoder

class TestBaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../openapi/')
        app.app.json_encoder = JSONEncoder
        app.add_api('openapi.yaml', pythonic_params=True)
        return app.app

    def test_create_app(self):
        self.assertIsNotNone(self.create_app())
        self.assertEqual(type(self.create_app()), type(connexion.FlaskApp(__name__)))

    def test_logging(self):
        logger = logging.getLogger('connexion.operation')
        self.assertEqual(logger.getEffectiveLevel(), logging.ERROR)

    def test_encoder(self):
        encoder = JSONEncoder()
        self.assertIsNotNone(encoder)

    def test_add_api(self):
        app = self.create_app()
        self.assertIsNotNone(app)
        with app.test_client() as client:
            response = client.get('/api/v1/ping')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'ping': 'pong'})

if __name__ == '__main__':
    unittest.main()