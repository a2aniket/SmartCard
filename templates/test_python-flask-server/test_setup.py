from python-flask-server.setup import *
import unittest
from unittest.mock import MagicMock
from openapi_server.__main__ import main

class TestSetup(unittest.TestCase):

    def test_main(self):
        # Test the main function
        main()

    def test_requires(self):
        # Test if required packages are installed
        self.assertTrue('connexion' in REQUIRES)
        self.assertTrue('swagger-ui-bundle' in REQUIRES)
        self.assertTrue('python_dateutil' in REQUIRES)

    def test_package_data(self):
        # Test if the package data is included
        self.assertTrue('openapi/openapi.yaml' in package_data[''])

    def test_entry_points(self):
        # Test if the entry points are correct
        self.assertEqual(entry_points['console_scripts'][0], 'openapi_server=openapi_server.__main__:main')

if __name__ == '__main__':
    unittest.main()