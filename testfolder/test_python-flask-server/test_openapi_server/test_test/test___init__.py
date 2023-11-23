from python-flask-server.openapi_server.test.__init__ import *
import unittest
import logging
import os
import sys
import json
import connexion
from openapi_server.encoder import JSONEncoder
from flask_testing import TestCase


class TestBase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../openapi/')
        app.app.json_encoder = JSONEncoder
        app.add_api('openapi.yaml', pythonic_params=True)
        return app.app

    def test_create_app(self):
        self.app = self.create_app()
        self.assertIsNotNone(self.app)

    def test_logger_level(self):
        logger = logging.getLogger('connexion.operation')
        self.assertEqual(logger.level, logging.ERROR)

    def test_json_encoder(self):
        encoder = JSONEncoder()
        self.assertIsNotNone(encoder)

    def test_api_spec(self):
        with open('../openapi/openapi.yaml', 'r') as f:
            spec = yaml.safe_load(f)
        self.assertIsNotNone(spec)

if __name__ == '__main__':
    unittest.main()