from python-flask-server.openapi_server.services.default_service import *
import unittest
from unittest.mock import patch
from openapi_server.services.default_service import DefaultService


class TestDefaultService(unittest.TestCase):

    def setUp(self):
        self.default_service = DefaultService()

    def test_get_default_list(self):
        with patch.object(DefaultService, 'get_default_list', return_value=[]):
            result = self.default_service.get_default_list()
            self.assertEqual(result, [])

    def test_get_default(self):
        with patch.object(DefaultService, 'get_default', return_value={'id': 1, 'name': 'default'}):
            result = self.default_service.get_default(1)
            self.assertEqual(result, {'id': 1, 'name': 'default'})

    def test_get_default_invalid_id(self):
        with self.assertRaises(Exception):
            self.default_service.get_default(-1)

    def test_get_default_not_found(self):
        with patch.object(DefaultService, 'get_default', return_value=None):
            with self.assertRaises(Exception):
                self.default_service.get_default(1)

    def test_add_default(self):
        with patch.object(DefaultService, 'add_default', return_value={'id': 1, 'name': 'default'}):
            result = self.default_service.add_default({'id': 1, 'name': 'default'})
            self.assertEqual(result, {'id': 1, 'name': 'default'})

    def test_add_default_already_exists(self):
        with patch.object(DefaultService, 'add_default', side_effect=Exception('Default with ID: 1 already exists')):
            with self.assertRaises(Exception):
                self.default_service.add_default({'id': 1, 'name': 'default'})

    def test_update_default(self):
        with patch.object(DefaultService, 'update_default', return_value={'id': 1, 'name': 'default updated'}):
            result = self.default_service.update_default({'id': 1, 'name': 'default updated'})
            self.assertEqual(result, {'id': 1, 'name': 'default updated'})

    def test_update_default_not_found(self):
        with patch.object(DefaultService, 'update_default', side_effect=Exception('Default with ID: 1 not found')):
            with self.assertRaises(Exception):
                self.default_service.update_default({'id': 1, 'name': 'default updated'})

    def test_delete_default(self):
        with patch.object(DefaultService, 'delete_default', return_value='Default with ID: 1 successfully deleted'):
            result = self.default_service.delete_default(1)
            self.assertEqual(result, 'Default with ID: 1 successfully deleted')

    def test_delete_default_not_found(self):
        with patch.object(DefaultService, 'delete_default', side_effect=Exception('Default with ID: 1 not found')):
            with self.assertRaises(Exception):
                self.default_service.delete_default(1)


if __name__ == '__main__':
    unittest.main()