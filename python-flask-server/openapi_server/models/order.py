# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from openapi_server.config_test import db, ma


class Order(db.Model):
    """Order - a model defined in OpenAPI

    :param id: The id of this Order.  # noqa: E501
    :param quantity: The quantity of this Order.  # noqa: E501
    :param ship_date: The ship_date of this Order.  # noqa: E501
    :param complete: The complete of this Order.  # noqa: E501
    """
    __tablename__ = 'Order'
    id = db.Column(db.Integer
, primary_key=True)
    quantity = db.Column(db.Integer
, nullable=False)
    ship_date = db.Column(db.String
, nullable=False)
    complete = db.Column(db.Boolean
, nullable=False)

'''
Serialize the Modeled Data With Marshmallow
Marshmallow finds attributes in the CourseController class and learns the types of those attributes 
so it knows how to serialize and deserialize them
'''
class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True
        sqla_session = db.session

Order_schema = OrderSchema()
Orders_schema = OrderSchema(many=True)

