from __init__ import *
import unittest
import logging

import connexion
from flask_testing import TestCase

from openapi_server.encoder import JSONEncoder


class TestBaseTestCase(TestCase):

    def test_create_app(self):
        """
        Test create_app function
        """
        app = self.create_app()
        self.assertIsNotNone(app)

    def test_logging_level(self):
        """
        Test logging level of connexion.operation
        """
        app = self.create_app()
        logger = logging.getLogger('connexion.operation')
        self.assertEqual(logger.getEffectiveLevel(), logging.ERROR)

    def test_json_encoder(self):
        """
        Test JSONEncoder
        """
        app = self.create_app()
        json_encoder = app.json_encoder
        self.assertIsInstance(json_encoder, JSONEncoder)

    def test_add_api(self):
        """
        Test add_api function
        """
        app = self.create_app()
        app.add_api('openapi.yaml', pythonic_params=True)
        self.assertIsNotNone(app.url_map)

    def test_pythonic_params(self):
        """
        Test pythonic_params parameter of add_api function
        """
        app = self.create_app()
        app.add_api('openapi.yaml', pythonic_params=True)
        self.assertIsNotNone(app.url_map)

    def test_openapi_yaml(self):
        """
        Test openapi.yaml file
        """
        app = self.create_app()
        spec_dir = app.config['SPECIFICATION_DIR']
        spec_file = spec_dir / 'openapi.yaml'
        self.assertTrue(spec_file.exists())