from python-flask-server.openapi_server.services.default_service import *
import unittest
from unittest.mock import patch, MagicMock
from openapi_server.services import pagination_sorting
from openapi_server.models.default import Default, Default_schema, Defaults_schema
from openapi_server.config_test import db
from openapi_server import app

class TestDefaultService(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_default_list(self):
        with patch('openapi_server.services.pagination_sorting.pagination_sorting', MagicMock(return_value=[{"id": 1, "name": "default1"}, {"id": 2, "name": "default2"}])):
            result = DefaultService.get_default_list()
            self.assertEqual(result, Defaults_schema.dump([{"id": 1, "name": "default1"}, {"id": 2, "name": "default2"}]))

    def test_get_default(self):
        default = Default(id=1, name="default1")
        db.session.add(default)
        db.session.commit()

        result = DefaultService.get_default(1)
        self.assertEqual(result, Default_schema.dump(default))

        with self.assertRaisesRegex(Exception, 'Default with ID: 0 does not exist'):
            DefaultService.get_default(0)

    def test_add_default(self):
        default = {"id": 1, "name": "default1"}

        result = DefaultService.add_default(default)
        self.assertEqual(result, Default_schema.dump(Default.query.get(1)))

        with self.assertRaisesRegex(Exception, 'Default with ID: 1 already exists'):
            DefaultService.add_default(default)

    def test_update_default(self):
        default = Default(id=1, name="default1")
        db.session.add(default)
        db.session.commit()

        update_default = {"id": 1, "name": "updated_default1"}

        result = DefaultService.update_default(update_default)
        self.assertEqual(result, Default_schema.dump(default))

        with self.assertRaisesRegex(Exception, 'Default with ID: 0 not found'):
            DefaultService.update_default({"id": 0, "name": "updated_default1"})

    def test_delete_default(self):
        default = Default(id=1, name="default1")
        db.session.add(default)
        db.session.commit()

        result = DefaultService.delete_default(1)
        self.assertEqual(result, 'Default with ID: 1 successfully deleted')

        with self.assertRaisesRegex(Exception, 'Default with ID: 0 not found'):
            DefaultService.delete_default(0)