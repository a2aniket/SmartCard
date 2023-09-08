# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from openapi_server.config_test import db, ma


class Pet(db.Model):
    """Pet - a model defined in OpenAPI

    :param id: The id of this Pet.  # noqa: E501
    :param name: The name of this Pet.  # noqa: E501
    :param breed: The breed of this Pet.  # noqa: E501
    :param age: The age of this Pet.  # noqa: E501
    :param price: The price of this Pet.  # noqa: E501
    """
    __tablename__ = 'Pet'
    id = db.Column(db.Integer
, primary_key=True)
    name = db.Column(db.String
, nullable=False)
    breed = db.Column(db.String
, nullable=False)
    age = db.Column(db.Integer
, nullable=False)
    price = db.Column(db.Integer
, nullable=False)

'''
Serialize the Modeled Data With Marshmallow
Marshmallow finds attributes in the CourseController class and learns the types of those attributes 
so it knows how to serialize and deserialize them
'''
class PetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pet
        load_instance = True
        sqla_session = db.session

Pet_schema = PetSchema()
Pets_schema = PetSchema(many=True)

