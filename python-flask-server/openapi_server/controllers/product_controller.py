import connexion
from flask import jsonify, request

from openapi_server.services.product_service import ProductService
from openapi_server.config_test import app


@app.route('/api/v3/product', methods=['POST'])
def add_product():  # noqa: E501
    """
    Services the add_product API GET call.
    """
    product = request.get_json()

    return jsonify(ProductService.add_product(product)), 200

@app.route('/api/v3/product/{product_id}', methods=['DELETE'])
def delete_product(product_id):  # noqa: E501
    """
    Services the delete_product API GET call.
    """

    return jsonify(ProductService.delete_product(product_id)), 200

@app.route('/api/v3/product/{product_id}', methods=['GET'])
def get_product(product_id):  # noqa: E501
    """
    Services the get_product API GET call.
    """

    return jsonify(ProductService.get_product(product_id)), 200

@app.route('/api/v3/product', methods=['GET'])
def get_product_list():  # noqa: E501
    """
    Services the get_product_list API GET call.
    """

    return jsonify(ProductService.get_product_list()), 200

@app.route('/api/v3/product', methods=['PUT'])
def update_product():  # noqa: E501
    """
    Services the update_product API GET call.
    """
    product = request.get_json()

    return jsonify(ProductService.update_product(product)), 200
