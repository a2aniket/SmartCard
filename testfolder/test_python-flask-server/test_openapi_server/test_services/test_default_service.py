from python-flask-server.openapi_server.services.default_service import *
import unittest
from unittest.mock import Mock
from openapi_server.services.pagination_sorting import pagination_sorting
from openapi_server.models.default import Default_schema, Defaults_schema
from openapi_server.config_test import db
from openapi_server.default_service import DefaultService


class TestDefaultService(unittest.TestCase):

    def setUp(self):
        self.default_service = DefaultService()
        self.default = {"id": 1, "name": "test_default"}

    def test_get_default_list(self):
        # Test case for getting list of defaults
        db.session.query(Default).delete()
        db.session.commit()
        self.assertEqual(self.default_service.get_default_list(), [])
        db.session.add(Default(**self.default))
        db.session.commit()
        expected_result = Defaults_schema.dump(pagination_sorting(Default))
        self.assertEqual(self.default_service.get_default_list(), expected_result)

    def test_get_default(self):
        # Test case for getting default by id
        db.session.query(Default).delete()
        db.session.commit()
        self.assertRaises(Exception, self.default_service.get_default, 1)
        db.session.add(Default(**self.default))
        db.session.commit()
        expected_result = Default_schema.dump(Default.query.filter(Default.id == 1).one_or_none())
        self.assertEqual(self.default_service.get_default(1), expected_result)

    def test_add_default(self):
        # Test case for adding a new default
        db.session.query(Default).delete()
        db.session.commit()
        result = self.default_service.add_default(self.default)
        self.assertEqual(result, Default_schema.dump(Default.query.filter(Default.id == 1).one_or_none()))
        self.assertRaises(Exception, self.default_service.add_default, self.default)

    def test_update_default(self):
        # Test case for updating a default by id
        db.session.query(Default).delete()
        db.session.commit()
        self.assertRaises(Exception, self.default_service.update_default, self.default)
        db.session.add(Default(**self.default))
        db.session.commit()
        self.default["name"] = "updated_default"
        expected_result = Default_schema.dump(Default.query.filter(Default.id == 1).one_or_none())
        self.assertEqual(self.default_service.update_default(self.default), expected_result)

    def test_delete_default(self):
        # Test case for deleting a default by id
        db.session.query(Default).delete()
        db.session.commit()
        self.assertRaises(Exception, self.default_service.delete_default, 1)
        db.session.add(Default(**self.default))
        db.session.commit()
        self.assertEqual(self.default_service.delete_default(1), "Default with ID: 1 successfully deleted")
        self.assertRaises(Exception, self.default_service.delete_default, 1)