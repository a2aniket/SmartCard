import connexion
from flask import jsonify, request

from openapi_server.services.default_service import DefaultService
from openapi_server.config_test import app


@app.route('/v1/apigen/generate/code', methods=['POST'])
def generate_code_post():  # noqa: E501
    """
    Services the generate_code_post API GET call.
    """
    generate_code_post_request = request.get_json()

    return "This method is not implemented as a service!"
