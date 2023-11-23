from python-flask-server.openapi_server.test.__init__ import *
import logging
import unittest.mock as mock
import pytest
import connexion
from flask_testing import TestCase
from openapi_server.encoder import JSONEncoder

class TestBaseTestCase(TestCase):
    
    def setUp(self):
        self.app = self.create_app()
        self.client = self.app.test_client()

    def test_logging(self):
        #Test if logging level is set to ERROR
        logger = logging.getLogger('connexion.operation')
        self.assertEqual(logger.level, logging.ERROR)

    def test_create_app(self):
        #Test if the app is created successfully
        app = self.create_app()
        self.assertIsNotNone(app)

    def test_app_json_encoder(self):
        #Test if the app json encoder is set to JSONEncoder
        app = self.create_app()
        self.assertEqual(app.json_encoder, JSONEncoder)

    def test_add_api(self):
        #Test if api is added to the app successfully
        app = self.create_app()
        with mock.patch('connexion.App.add_api') as mock_add_api:
            app = self.create_app()
            mock_add_api.assert_called_once_with('openapi.yaml', pythonic_params=True)