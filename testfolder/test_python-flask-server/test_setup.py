from python-flask-server.setup import *
import unittest

class TestSetup(unittest.TestCase):
    
    def test_name(self):
        self.assertEqual(NAME, "openapi_server")
    
    def test_version(self):
        self.assertEqual(VERSION, "1.0.0")
    
    def test_requires(self):
        self.assertIn("connexion>=2.0.2", REQUIRES)
        self.assertIn("swagger-ui-bundle>=0.0.2", REQUIRES)
        self.assertIn("python_dateutil>=2.6.0", REQUIRES)
    
    def test_package_data(self):
        self.assertDictEqual(package_data, {'': ['openapi/openapi.yaml']})
    
    def test_include_package_data(self):
        self.assertTrue(include_package_data)
    
    def test_entry_points(self):
        self.assertDictEqual(entry_points, {'console_scripts': ['openapi_server=openapi_server.__main__:main']})
    
    def test_long_description(self):
        self.assertIsNotNone(long_description)

if __name__ == '__main__':
    unittest.main()