from python-flask-server.openapi_server.test.__init__ import *
import logging
import unittest
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

class TestAPI(TestBase):
    def test_create_app(self):
        """
        Test that the app is created correctly
        """
        self.assertIsNotNone(self.create_app())

    def test_json_encoder(self):
        """
        Test that the JSONEncoder is correctly set on the app
        """
        app = self.create_app()
        self.assertIsInstance(app.json_encoder, JSONEncoder)

    def test_add_api(self):
        """
        Test that the API is correctly added to the app
        """
        app = self.create_app()
        self.assertIsNotNone(app.url_map)

    def test_logging(self):
        """
        Test that the logging level is set correctly
        """
        logger = logging.getLogger('connexion.operation')
        self.assertEqual(logger.level, logging.ERROR)

    def test_pythonic_params(self):
        """
        Test that pythonic_params is set correctly
        """
        app = self.create_app()
        self.assertTrue(app.config['PYTHONIC_PARAMS'])