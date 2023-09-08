import connexion
from flask import jsonify, request

from openapi_server.services.category_service import CategoryService
from openapi_server.config_test import app


@app.route('/api/v3/category', methods=['POST'])
def add_category():  # noqa: E501
    """
    Services the add_category API GET call.
    """
    category = request.get_json()

    return jsonify(CategoryService.add_category(category)), 200

@app.route('/api/v3/category/{category_id}', methods=['DELETE'])
def delete_category(category_id):  # noqa: E501
    """
    Services the delete_category API GET call.
    """

    return jsonify(CategoryService.delete_category(category_id)), 200

@app.route('/api/v3/category/{category_id}', methods=['GET'])
def get_category(category_id):  # noqa: E501
    """
    Services the get_category API GET call.
    """

    return jsonify(CategoryService.get_category(category_id)), 200

@app.route('/api/v3/category', methods=['GET'])
def get_category_list():  # noqa: E501
    """
    Services the get_category_list API GET call.
    """

    return jsonify(CategoryService.get_category_list()), 200

@app.route('/api/v3/category', methods=['PUT'])
def update_category():  # noqa: E501
    """
    Services the update_category API GET call.
    """
    category = request.get_json()

    return jsonify(CategoryService.update_category(category)), 200
