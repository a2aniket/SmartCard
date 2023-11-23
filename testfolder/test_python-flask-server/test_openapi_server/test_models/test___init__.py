from python-flask-server.openapi_server.models.__init__ import *
def test_imports():
    """
    Test if all necessary imports are present
    """
    import openapi_server.models.generate_code_post200_response
    import openapi_server.models.generate_code_post400_response
    import openapi_server.models.generate_code_post_request
    import openapi_server.models.user
    import openapi_server.config_test
    from openapi_server.models.generate_code_post200_response import GenerateCodePost200Response, GenerateCodePost200Response_schema, GenerateCodePost200Responses_schema
    from openapi_server.models.generate_code_post400_response import GenerateCodePost400Response, GenerateCodePost400Response_schema, GenerateCodePost400Responses_schema
    from openapi_server.models.generate_code_post_request import GenerateCodePostRequest, GenerateCodePostRequest_schema, GenerateCodePostRequests_schema
    from openapi_server.models.user import User
    from openapi_server.config_test import db, app

def test_db_creation():
    """
    Test if the database is created successfully
    """
    with app.app_context():
        assert db.create_all() == None