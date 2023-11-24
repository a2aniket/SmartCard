from python-flask-server.setup import *
import unittest

class TestOpenAPI(unittest.TestCase):

    def test_name(self):
        self.assertEqual(NAME, "openapi_server")

    def test_version(self):
        self.assertEqual(VERSION, "1.0.0")

    def test_requires(self):
        self.assertIn("connexion>=2.0.2", REQUIRES)
        self.assertIn("swagger-ui-bundle>=0.0.2", REQUIRES)
        self.assertIn("python_dateutil>=2.6.0", REQUIRES)

    def test_description(self):
        self.assertIn("Swagger", DESCRIPTION)
        self.assertIn("OpenAPI 3.0", DESCRIPTION)

    def test_author_email(self):
        self.assertEqual(AUTHOR_EMAIL, "")

    def test_url(self):
        self.assertEqual(URL, "")

    def test_keywords(self):
        self.assertIn("OpenAPI", KEYWORDS)
        self.assertIn("Swagger", KEYWORDS)
        self.assertIn("Student Management System", KEYWORDS)
        self.assertIn("OpenAPI 3.0", KEYWORDS)

    def test_packages(self):
        self.assertIn("openapi_server", PACKAGES)

    def test_package_data(self):
        self.assertIn("openapi/openapi.yaml", PACKAGE_DATA[""])

    def test_include_package_data(self):
        self.assertTrue(INCLUDE_PACKAGE_DATA)

    def test_entry_points(self):
        self.assertIn("console_scripts", ENTRY_POINTS)
        self.assertIn("openapi_server=openapi_server.__main__:main", ENTRY_POINTS["console_scripts"])

    def test_long_description(self):
        self.assertIn("Openapi Generator", LONG_DESCRIPTION)