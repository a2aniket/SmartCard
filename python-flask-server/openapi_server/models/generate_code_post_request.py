# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from openapi_server.config_test import db, ma


class GenerateCodePostRequest(db.Model):
    """GenerateCodePostRequest - a model defined in OpenAPI

    :param language: The language of this GenerateCodePostRequest.  # noqa: E501
    :param open_api_url: The open_api_url of this GenerateCodePostRequest.  # noqa: E501
    """
    __tablename__ = 'GenerateCodePostRequest'
    language = db.Column(db.String
, nullable=False)
    open_api_url = db.Column(db.String
, nullable=False)

'''
Serialize the Modeled Data With Marshmallow
Marshmallow finds attributes in the CourseController class and learns the types of those attributes 
so it knows how to serialize and deserialize them
'''
class GenerateCodePostRequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GenerateCodePostRequest
        load_instance = True
        sqla_session = db.session

GenerateCodePostRequest_schema = GenerateCodePostRequestSchema()
GenerateCodePostRequests_schema = GenerateCodePostRequestSchema(many=True)

