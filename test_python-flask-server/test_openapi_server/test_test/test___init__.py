from python-flask-server.openapi_server.test.__init__ import *
import unittest
import logging
import connexion
from flask_testing import TestCase
from openapi_server.encoder import JSONEncoder


class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../openapi/')
        app.app.json_encoder = JSONEncoder
        app.add_api('openapi.yaml', pythonic_params=True)
        return app.app


class TestBaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = BaseTestCase().create_app()
        self.client = self.app.test_client()

    def test_logging_level(self):
        self.assertEqual(logging.getLogger('connexion.operation').getEffectiveLevel(), logging.ERROR)

    def test_app_json_encoder(self):
        self.assertIsInstance(self.app.json_encoder, JSONEncoder)

    def test_add_api(self):
        self.assertIn('openapi.yaml', self.app.extensions['flask-connexion']['specs'][0]['spec']['info']['title'])

    def test_pythonic_params(self):
        self.assertTrue(self.app.extensions['flask-connexion']['pythonic_params'])

    def test_api_call(self):
        response = self.client.get('/api/v1/test')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"message": "Test successful"', response.data)


if __name__ == '__main__':
    unittest.main()