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

    def test_logger_level(self):
        self.assertEqual(logging.getLogger('connexion.operation').getEffectiveLevel(), logging.ERROR)

    def test_app_json_encoder(self):
        app = self.create_app()
        self.assertIsInstance(app.json_encoder, JSONEncoder)

    def test_add_api(self):
        app = self.create_app()
        with app.app_context():
            self.assertIsNotNone(connexion.get_swagger_ui_blueprint())

    def test_pythonic_params(self):
        app = self.create_app()
        with app.app_context():
            self.assertTrue(connexion.get_option('pythonic_params'))

if __name__ == '__main__':
    unittest.main()