import connexion
from flask import jsonify, request

from openapi_server.services.order_service import OrderService
from openapi_server.config_test import app


@app.route('/api/v3/order', methods=['POST'])
def add_order():  # noqa: E501
    """
    Services the add_order API GET call.
    """
    order = request.get_json()

    return jsonify(OrderService.add_order(order)), 200

@app.route('/api/v3/order/{order_id}', methods=['DELETE'])
def delete_order(order_id):  # noqa: E501
    """
    Services the delete_order API GET call.
    """

    return jsonify(OrderService.delete_order(order_id)), 200

@app.route('/api/v3/order/{order_id}', methods=['GET'])
def get_order(order_id):  # noqa: E501
    """
    Services the get_order API GET call.
    """

    return jsonify(OrderService.get_order(order_id)), 200

@app.route('/api/v3/order', methods=['GET'])
def get_order_list():  # noqa: E501
    """
    Services the get_order_list API GET call.
    """

    return jsonify(OrderService.get_order_list()), 200

@app.route('/api/v3/order', methods=['PUT'])
def update_order():  # noqa: E501
    """
    Services the update_order API GET call.
    """
    order = request.get_json()

    return jsonify(OrderService.update_order(order)), 200
