from python-flask-server.openapi_server.services.default_service import *
import unittest
from unittest.mock import MagicMock
from openapi_server.services.pagination_sorting import pagination_sorting
from openapi_server.models.default import Default, Default_schema, Defaults_schema
from openapi_server.config_test import db
from app import app

class TestDefaultService(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.init_app(app)
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_default_list(self):
        with app.app_context():
            sample_data = {
                "id": 1,
                "name": "Test",
                "type": "Test Type"
            }
            db.session.add(Default_schema.load(sample_data, session=db.session))
            db.session.commit()
            response = app.test_client().get('/api/v1/defaults')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 1)

    def test_get_default(self):
        with app.app_context():
            sample_data = {
                "id": 1,
                "name": "Test",
                "type": "Test Type"
            }
            db.session.add(Default_schema.load(sample_data, session=db.session))
            db.session.commit()
            response = app.test_client().get('/api/v1/defaults/1')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['id'], 1)

    def test_add_default(self):
        with app.app_context():
            sample_data = {
                "id": 1,
                "name": "Test",
                "type": "Test Type"
            }
            response = app.test_client().post('/api/v1/defaults', json=sample_data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['id'], 1)

    def test_add_existing_default(self):
        with app.app_context():
            sample_data = {
                "id": 1,
                "name": "Test",
                "type": "Test Type"
            }
            db.session.add(Default_schema.load(sample_data, session=db.session))
            db.session.commit()
            response = app.test_client().post('/api/v1/defaults', json=sample_data)
            self.assertEqual(response.status_code, 400)

    def test_update_default(self):
        with app.app_context():
            sample_data = {
                "id": 1,
                "name": "Test",
                "type": "Test Type"
            }
            db.session.add(Default_schema.load(sample_data, session=db.session))
            db.session.commit()
            update_data = {
                "id": 1,
                "name": "Updated Test",
                "type": "Updated Test Type"
            }
            response = app.test_client().put('/api/v1/defaults', json=update_data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['name'], "Updated Test")
            self.assertEqual(response.json['type'], "Updated Test Type")

    def test_update_non_existing_default(self):
        with app.app_context():
            update_data = {
                "id": 1,
                "name": "Updated Test",
                "type": "Updated Test Type"
            }
            response = app.test_client().put('/api/v1/defaults', json=update_data)
            self.assertEqual(response.status_code, 404)

    def test_delete_default(self):
        with app.app_context():
            sample_data = {
                "id": 1,
                "name": "Test",
                "type": "Test Type"
            }
            db.session.add(Default_schema.load(sample_data, session=db.session))
            db.session.commit()
            response = app.test_client().delete('/api/v1/defaults/1')
            self.assertEqual(response.status_code, 200)

    def test_delete_non_existing_default(self):
        with app.app_context():
            response = app.test_client().delete('/api/v1/defaults/1')
            self.assertEqual(response.status_code, 400)