# coding: utf-8

# flake8: noqa
from __future__ import absolute_import
# import models into model package
from openapi_server.models.generate_code_post200_response import GenerateCodePost200Response, GenerateCodePost200Response_schema, GenerateCodePost200Responses_schema
from openapi_server.models.generate_code_post400_response import GenerateCodePost400Response, GenerateCodePost400Response_schema, GenerateCodePost400Responses_schema
from openapi_server.models.generate_code_post_request import GenerateCodePostRequest, GenerateCodePostRequest_schema, GenerateCodePostRequests_schema

from openapi_server.models.user import User
from openapi_server.config_test import db, app

with app.app_context():
    db.create_all()