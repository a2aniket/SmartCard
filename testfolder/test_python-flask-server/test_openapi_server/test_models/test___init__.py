from python-flask-server.openapi_server.models.__init__ import *
def test_models_import():
    """
    Test that models are imported correctly
    """
    from openapi_server.models.generate_code_post200_response import GenerateCodePost200Response
    from openapi_server.models.generate_code_post400_response import GenerateCodePost400Response
    from openapi_server.models.generate_code_post_request import GenerateCodePostRequest
    from openapi_server.models.user import User
    
    assert GenerateCodePost200Response
    assert GenerateCodePost400Response
    assert GenerateCodePostRequest
    assert User

def test_database_creation():
    """
    Test that the database is created correctly
    """
    from openapi_server.config_test import db, app
    
    with app.app_context():
        db.create_all()
        assert db.engine.table_names() == ['user']

def test_generate_code_post200_response_schema():
    """
    Test that GenerateCodePost200Response schema is correct
    """
    from openapi_server.models.generate_code_post200_response import GenerateCodePost200Response, GenerateCodePost200Response_schema
    
    data = {"message": "Success"}
    response = GenerateCodePost200Response(**data)
    schema = GenerateCodePost200Response_schema()
    
    assert schema.dump(response) == {'message': 'Success'}

def test_generate_code_post400_response_schema():
    """
    Test that GenerateCodePost400Response schema is correct
    """
    from openapi_server.models.generate_code_post400_response import GenerateCodePost400Response, GenerateCodePost400Response_schema
    
    data = {"message": "Error"}
    response = GenerateCodePost400Response(**data)
    schema = GenerateCodePost400Response_schema()
    
    assert schema.dump(response) == {'message': 'Error'}

def test_generate_code_post_request_schema():
    """
    Test that GenerateCodePostRequest schema is correct
    """
    from openapi_server.models.generate_code_post_request import GenerateCodePostRequest, GenerateCodePostRequest_schema
    
    data = {"language": "Python", "code": "print('Hello, World!')"}
    request = GenerateCodePostRequest(**data)
    schema = GenerateCodePostRequest_schema()
    
    assert schema.dump(request) == {'code': "print('Hello, World!')", 'language': 'Python'}

def test_user_model():
    """
    Test that User model is created and data can be added and retrieved
    """
    from openapi_server.models.user import User
    from openapi_server.config_test import db, app
    
    with app.app_context():
        db.create_all()
        user = User(username='test_user', email='test_user@example.com', password='123456')
        db.session.add(user)
        db.session.commit()
        assert User.query.filter_by(username='test_user').first() is not None