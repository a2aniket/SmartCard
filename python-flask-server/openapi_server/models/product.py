# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from openapi_server.config_test import db, ma


class Product(db.Model):
    """Product - a model defined in OpenAPI

    :param id: The id of this Product.  # noqa: E501
    :param name: The name of this Product.  # noqa: E501
    :param quantity: The quantity of this Product.  # noqa: E501
    :param price: The price of this Product.  # noqa: E501
    """
    __tablename__ = 'Product'
    id = db.Column(db.Integer
, primary_key=True)
    name = db.Column(db.String
, nullable=False)
    quantity = db.Column(db.Integer
, nullable=False)
    price = db.Column(db.Integer
, nullable=False)

'''
Serialize the Modeled Data With Marshmallow
Marshmallow finds attributes in the CourseController class and learns the types of those attributes 
so it knows how to serialize and deserialize them
'''
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True
        sqla_session = db.session

Product_schema = ProductSchema()
Products_schema = ProductSchema(many=True)

