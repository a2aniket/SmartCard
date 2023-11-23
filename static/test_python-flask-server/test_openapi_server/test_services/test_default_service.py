from python-flask-server.openapi_server.services.default_service import *
import unittest
from unittest.mock import patch
from openapi_server.services.default_service import DefaultService

class TestDefaultService(unittest.TestCase):
    
    def setUp(self):
        self.default_service = DefaultService()
        self.default_data = {
            "id": 1,
            "name": "Test Default",
            "amount": 1000.0,
            "created": "2022-01-01 00:00:00",
            "modified": "2022-01-01 00:00:00"
        }
        self.default = self.default_service.add_default(self.default_data)

    def test_get_default_list(self):
        result = self.default_service.get_default_list()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)

    def test_get_default(self):
        result = self.default_service.get_default(self.default["id"])
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)

    def test_add_default(self):
        new_default = {
            "id": 2,
            "name": "Test Default 2",
            "amount": 2000.0,
            "created": "2022-01-02 00:00:00",
            "modified": "2022-01-02 00:00:00"
        }
        result = self.default_service.add_default(new_default)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)

    def test_add_default_duplicate_id(self):
        with self.assertRaises(Exception):
            self.default_service.add_default(self.default_data)

    def test_update_default(self):
        self.default_data["name"] = "Updated Test Default"
        result = self.default_service.update_default(self.default_data)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["name"], "Updated Test Default")

    def test_update_default_not_found(self):
        self.default_data["id"] = 9999
        with self.assertRaises(Exception):
            self.default_service.update_default(self.default_data)

    def test_delete_default(self):
        result = self.default_service.delete_default(self.default["id"])
        self.assertIsNotNone(result)
        self.assertEqual(result, f"Default with ID: {self.default['id']} successfully deleted")
        with self.assertRaises(Exception):
            self.default_service.get_default(self.default["id"])

    def test_delete_default_not_found(self):
        with self.assertRaises(Exception):
            self.default_service.delete_default(9999)