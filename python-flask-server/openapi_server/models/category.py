# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from openapi_server.config_test import db, ma


class Category(db.Model):
    """Category - a model defined in OpenAPI

    :param id: The id of this Category.  # noqa: E501
    :param name: The name of this Category.  # noqa: E501
    """
    __tablename__ = 'Category'
    id = db.Column(db.Integer
, primary_key=True)
    name = db.Column(db.String
, nullable=False)

'''
Serialize the Modeled Data With Marshmallow
Marshmallow finds attributes in the CourseController class and learns the types of those attributes 
so it knows how to serialize and deserialize them
'''
class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        load_instance = True
        sqla_session = db.session

Category_schema = CategorySchema()
Categorys_schema = CategorySchema(many=True)

