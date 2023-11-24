from python-flask-server.openapi_server.test.__init__ import *
import unittest
import logging

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

    def test_create_app(self):
        """
        Test that creates a flask app instance
        """
        app = self.create_app()
        self.assertIsNotNone(app)

    def test_logging_level(self):
        """
        Test that checks logging level
        """
        logger = logging.getLogger('connexion.operation')
        self.assertEqual(logger.level, logging.ERROR)

    def test_add_api(self):
        """
        Test that checks if api is added
        """
        app = self.create_app()
        self.assertTrue('openapi.yaml' in app.url_map._rules_by_endpoint)

    def test_json_encoder(self):
        """
        Test that checks JSONEncoder instance
        """
        app = self.create_app()
        self.assertIsInstance(app.json_encoder, JSONEncoder)

    def test_pythonic_params(self):
        """
        Test that checks if pythonic params are set
        """
        app = self.create_app()
        self.assertTrue(app.app.config['PYTHONIC_PARAMS'])

if __name__ == '__main__':
    unittest.main()