import connexion
from flask import jsonify, request

from openapi_server.services.pet_service import PetService
from openapi_server.config_test import app


@app.route('/api/v3/pet', methods=['POST'])
def add_pet():  # noqa: E501
    """
    Services the add_pet API GET call.
    """
    pet = request.get_json()

    return jsonify(PetService.add_pet(pet)), 200

@app.route('/api/v3/pet/{pet_id}', methods=['DELETE'])
def delete_pet(pet_id):  # noqa: E501
    """
    Services the delete_pet API GET call.
    """

    return jsonify(PetService.delete_pet(pet_id)), 200

@app.route('/api/v3/pet/{pet_id}', methods=['GET'])
def get_pet(pet_id):  # noqa: E501
    """
    Services the get_pet API GET call.
    """

    return jsonify(PetService.get_pet(pet_id)), 200

@app.route('/api/v3/pet', methods=['GET'])
def get_pet_list():  # noqa: E501
    """
    Services the get_pet_list API GET call.
    """

    return jsonify(PetService.get_pet_list()), 200

@app.route('/api/v3/pet', methods=['PUT'])
def update_pet():  # noqa: E501
    """
    Services the update_pet API GET call.
    """
    pet = request.get_json()

    return jsonify(PetService.update_pet(pet)), 200
