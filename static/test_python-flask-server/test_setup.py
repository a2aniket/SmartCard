from python-flask-server.setup import *
import unittest
from unittest.mock import patch, MagicMock
from openapi_server.__main__ import main

class TestOpenAPIServer(unittest.TestCase):

    @patch('sys.argv', ['openapi_server', '--help'])
    def test_help_command(self):
        with self.assertRaises(SystemExit):
            main()

    @patch('sys.argv', ['openapi_server', 'run'])
    def test_run_command(self):
        with patch('openapi_server.__main__.connexion.FlaskApp.run') as mock_flask_run:
            main()
            mock_flask_run.assert_called_once()

    @patch('sys.argv', ['openapi_server', 'generate'])
    def test_generate_command(self):
        with patch('openapi_server.__main__.generate_api') as mock_generate:
            main()
            mock_generate.assert_called_once()

    @patch('sys.argv', ['openapi_server', 'not_a_valid_command'])
    def test_invalid_command(self):
        with self.assertRaises(SystemExit):
            main()

if __name__ == '__main__':
    unittest.main()