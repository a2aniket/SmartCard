# coding: utf-8

# flake8: noqa
from __future__ import absolute_import
# import models into model package
from openapi_server.models.category import Category, Category_schema, Categorys_schema
from openapi_server.models.order import Order, Order_schema, Orders_schema
from openapi_server.models.pet import Pet, Pet_schema, Pets_schema
from openapi_server.models.product import Product, Product_schema, Products_schema
from openapi_server.models.user import User, User_schema, Users_schema

from openapi_server.models.user import User
from openapi_server.config_test import db, app

with app.app_context():
    db.create_all()