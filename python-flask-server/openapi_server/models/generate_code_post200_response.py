# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from openapi_server.config_test import db, ma


class GenerateCodePost200Response(db.Model):
    """GenerateCodePost200Response - a model defined in OpenAPI

    :param message: The message of this GenerateCodePost200Response.  # noqa: E501
    """
    __tablename__ = 'GenerateCodePost200Response'
    message = db.Column(db.String
, nullable=False)

'''
Serialize the Modeled Data With Marshmallow
Marshmallow finds attributes in the CourseController class and learns the types of those attributes 
so it knows how to serialize and deserialize them
'''
class GenerateCodePost200ResponseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GenerateCodePost200Response
        load_instance = True
        sqla_session = db.session

GenerateCodePost200Response_schema = GenerateCodePost200ResponseSchema()
GenerateCodePost200Responses_schema = GenerateCodePost200ResponseSchema(many=True)

