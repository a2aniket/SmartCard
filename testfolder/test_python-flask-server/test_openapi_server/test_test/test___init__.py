from python-flask-server.openapi_server.test.__init__ import *
import unittest
import logging

import connexion
from flask_testing import TestCase

from openapi_server.encoder import JSONEncoder


class TestBaseCase(unittest.TestCase):

    def test_create_app(self):
        """
        Test that the create_app function returns a Flask app instance.
        """
        base_test_case = TestCase()
        app = base_test_case.create_app()
        self.assertIsInstance(app, connexion.FlaskApp)

    def test_create_app_logging(self):
        """
        Test that the create_app function sets the logging level of the connexion operation logger to ERROR.
        """
        base_test_case = TestCase()
        base_test_case.create_app()
        logger = logging.getLogger('connexion.operation')
        self.assertEqual(logger.getEffectiveLevel(), logging.ERROR)

    def test_create_app_json_encoder(self):
        """
        Test that the create_app function sets the JSONEncoder as the Flask app's JSON encoder.
        """
        base_test_case = TestCase()
        app = base_test_case.create_app()
        self.assertIsInstance(app.json_encoder, JSONEncoder)

    def test_create_app_add_api(self):
        """
        Test that the create_app function adds the API defined in the openapi.yaml file to the Flask app.
        """
        base_test_case = TestCase()
        app = base_test_case.create_app()
        self.assertIn('openapi.yaml', app.blueprints)

    def test_create_app_pythonic_params(self):
        """
        Test that the create_app function sets the pythonic_params flag to True when adding the API to the Flask app.
        """
        base_test_case = TestCase()
        app = base_test_case.create_app()
        blueprint = app.blueprints['openapi.yaml']
        self.assertTrue(blueprint.options.get('pythonic_params', False))