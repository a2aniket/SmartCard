# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.order import Order  # noqa: E501
from openapi_server.test import BaseTestCase


class TestOrder(BaseTestCase):
    """Order integration test stubs"""

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_order(self):
        """Test case for add_order

        Add a new order to the store
        """
        order = {"quantity":7,"id":1,"shipDate":"2000-01-23T04:56:07.000+00:00","complete":True}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3/order',
            method='POST',
            headers=headers,
            data=json.dumps(order),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_order(self):
        """Test case for delete_order

        Deletes a order
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3/order/{order_id}'.format(order_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_order(self):
        """Test case for get_order

        Find order by ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3/order/{order_id}'.format(order_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_order_list(self):
        """Test case for get_order_list

        Get list of all orders
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3/order',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_update_order(self):
        """Test case for update_order

        Update an existing order
        """
        order = {"quantity":7,"id":1,"shipDate":"2000-01-23T04:56:07.000+00:00","complete":True}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3/order',
            method='PUT',
            headers=headers,
            data=json.dumps(order),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
