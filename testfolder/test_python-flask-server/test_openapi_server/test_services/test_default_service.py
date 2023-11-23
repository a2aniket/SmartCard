from python-flask-server.openapi_server.services.default_service import *
import unittest
from unittest.mock import MagicMock
from openapi_server.services.pagination_sorting import pagination_sorting
from openapi_server.models.default import Default_schema, Defaults_schema
from openapi_server.config_test import db
from openapi_server import app
from flask import json

class TestDefaultService(unittest.TestCase):

    # Test for retrieving a list of defaults
    def test_get_default_list(self):
        with app.app_context():
            # Mocking pagination_sorting function
            pagination_sorting = MagicMock(return_value=[{"id": 1, "name": "Default 1", "amount": 100}])

            # Calling the function under test
            result = app.DefaultService.get_default_list()

            # Verifying the returned result
            self.assertEqual(result.status_code, 200)
            self.assertEqual(result.content_type, "application/json")
            self.assertEqual(json.loads(result.data), Defaults_schema.dump([{"id": 1, "name": "Default 1", "amount": 100}]))
            pagination_sorting.assert_called_once_with(Default)

    # Test for retrieving a default by ID
    def test_get_default(self):
        with app.app_context():
            # Adding a default to the database
            default = {"id": 1, "name": "Default 1", "amount": 100}
            app.DefaultService.add_default(default)

            # Calling the function under test
            result = app.DefaultService.get_default(1)

            # Verifying the returned result
            self.assertEqual(result.status_code, 200)
            self.assertEqual(result.content_type, "application/json")
            self.assertEqual(json.loads(result.data), Default_schema.dump({"id": 1, "name": "Default 1", "amount": 100}))

    # Test for adding a new default
    def test_add_default(self):
        with app.app_context():
            # Mocking load function of Default_schema
            Default_schema.load = MagicMock(return_value={"id": 1, "name": "Default 1", "amount": 100})

            # Calling the function under test
            result = app.DefaultService.add_default({"id": 1, "name": "Default 1", "amount": 100})

            # Verifying the returned result
            self.assertEqual(result.status_code, 200)
            self.assertEqual(result.content_type, "application/json")
            self.assertEqual(json.loads(result.data), Default_schema.dump({"id": 1, "name": "Default 1", "amount": 100}))
            Default_schema.load.assert_called_once_with({"id": 1, "name": "Default 1", "amount": 100}, session=db.session)

            # Adding the same default again to check if it raises 400 error
            with self.assertRaises(Exception) as context:
                app.DefaultService.add_default({"id": 1, "name": "Default 1", "amount": 100})
            self.assertEqual(str(context.exception), "Default with ID: 1 already exists")

    # Test for updating an existing default
    def test_update_default(self):
        with app.app_context():
            # Adding a default to the database
            default = {"id": 1, "name": "Default 1", "amount": 100}
            app.DefaultService.add_default(default)

            # Mocking load function of Default_schema
            Default_schema.load = MagicMock(return_value={"id": 1, "name": "Default 1 Updated", "amount": 200})

            # Calling the function under test
            result = app.DefaultService.update_default({"id": 1, "name": "Default 1 Updated", "amount": 200})

            # Verifying the returned result
            self.assertEqual(result.status_code, 200)
            self.assertEqual(result.content_type, "application/json")
            self.assertEqual(json.loads(result.data), Default_schema.dump({"id": 1, "name": "Default 1 Updated", "amount": 200}))
            Default_schema.load.assert_called_once_with({"id": 1, "name": "Default 1 Updated", "amount": 200}, session=db.session)

            # Updating a non-existing default
            with self.assertRaises(Exception) as context:
                app.DefaultService.update_default({"id": 2, "name": "Default 2", "amount": 300})
            self.assertEqual(str(context.exception), "Default with ID: 2 not found")

    # Test for deleting a default
    def test_delete_default(self):
        with app.app_context():
            # Adding a default to the database
            default = {"id": 1, "name": "Default 1", "amount": 100}
            app.DefaultService.add_default(default)

            # Calling the function under test
            result = app.DefaultService.delete_default(1)

            # Verifying the returned result
            self.assertEqual(result, "Default with ID: 1 successfully deleted")

            # Deleting a non-existing default
            with self.assertRaises(Exception) as context:
                app.DefaultService.delete_default(2)
            self.assertEqual(str(context.exception), "Default with ID: 2 not found")