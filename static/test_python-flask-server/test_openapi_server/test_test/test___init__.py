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
        app = self.create_app()
        self.assertIsNotNone(app)

    def test_logging(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        logger = logging.getLogger('connexion.operation')
        self.assertEqual(logger.level, logging.ERROR)

    def test_JSONEncoder(self):
        encoder = JSONEncoder()
        self.assertIsNotNone(encoder)

    def test_add_api(self):
        app = self.create_app()
        app.add_api('openapi.yaml', pythonic_params=True)
        self.assertIsNotNone(app)