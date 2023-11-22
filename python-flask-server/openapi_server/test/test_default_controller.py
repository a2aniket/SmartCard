# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.generate_code_post200_response import GenerateCodePost200Response  # noqa: E501
from openapi_server.models.generate_code_post400_response import GenerateCodePost400Response  # noqa: E501
from openapi_server.models.generate_code_post_request import GenerateCodePostRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefault(BaseTestCase):
    """Default integration test stubs"""

    def test_generate_code_post(self):
        """Test case for generate_code_post

        Generate code from OpenAPI specification
        """
        generate_code_post_request = openapi_server.GenerateCodePostRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/v1/apigen/generate/code',
            method='POST',
            headers=headers,
            data=json.dumps(generate_code_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
