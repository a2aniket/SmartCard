from python-flask-server.openapi_server.test.__init__ import *
import unittest
import logging

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
        # Test if the app is created successfully
        app = self.create_app()
        self.assertIsNotNone(app)

    def test_logging(self):
        # Test if logging is set to ERROR level
        logger = logging.getLogger('connexion.operation')
        self.assertEqual(logger.level, logging.ERROR)

    def test_json_encoder(self):
        # Test if JSONEncoder is used for JSON encoding
        app = self.create_app()
        self.assertIsInstance(app.json_encoder, JSONEncoder)

    def test_add_api(self):
        # Test if API is added successfully
        app = self.create_app()
        self.assertIsNotNone(app.url_map)

    def test_pythonic_params(self):
        # Test if pythonic_params is set to True
        app = self.create_app()
        self.assertTrue(app.config['PYTHONIC_PARAMS'])