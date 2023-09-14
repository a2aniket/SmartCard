# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from openapi_server.config_test import db, ma


class GenerateCodePost400Response(db.Model):
    """GenerateCodePost400Response - a model defined in OpenAPI

    :param message: The message of this GenerateCodePost400Response.  # noqa: E501
    """
    __tablename__ = 'GenerateCodePost400Response'
    message = db.Column(db.String
, nullable=False)

'''
Serialize the Modeled Data With Marshmallow
Marshmallow finds attributes in the CourseController class and learns the types of those attributes 
so it knows how to serialize and deserialize them
'''
class GenerateCodePost400ResponseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GenerateCodePost400Response
        load_instance = True
        sqla_session = db.session

GenerateCodePost400Response_schema = GenerateCodePost400ResponseSchema()
GenerateCodePost400Responses_schema = GenerateCodePost400ResponseSchema(many=True)

