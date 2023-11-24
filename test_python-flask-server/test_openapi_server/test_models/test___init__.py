from python-flask-server.openapi_server.models.__init__ import *
def test_generate_code_post200_response():
    """
    Test the GenerateCodePost200Response model
    """
    response = GenerateCodePost200Response(
        success=True,
        message="Code generation successful",
        data={"code": "print('Hello World!')"})

    assert response.success == True
    assert response.message == "Code generation successful"
    assert response.data == {"code": "print('Hello World!')"}

def test_generate_code_post400_response():
    """
    Test the GenerateCodePost400Response model
    """
    response = GenerateCodePost400Response(
        success=False,
        message="Invalid request parameters",
        data={"errors": ["Missing required field: 'language'"]})

    assert response.success == False
    assert response.message == "Invalid request parameters"
    assert response.data == {"errors": ["Missing required field: 'language'"]}

def test_generate_code_post_request():
    """
    Test the GenerateCodePostRequest model
    """
    user = User(username="test_user", email="test_user@example.com")
    request = GenerateCodePostRequest(
        user=user,
        language="python",
        code_template="print('Hello {{ name }}!')",
        context={"name": "World"})

    assert request.user == user
    assert request.language == "python"
    assert request.code_template == "print('Hello {{ name }}!')"
    assert request.context == {"name": "World"}

def test_generate_code_post_request_missing_field():
    """
    Test GenerateCodePostRequest with missing required field
    """
    user = User(username="test_user", email="test_user@example.com")
    try:
        request = GenerateCodePostRequest(
            user=user,
            code_template="print('Hello {{ name }}!')",
            context={"name": "World"})
    except ValueError as e:
        assert str(e) == "Missing required field: 'language'"
    else:
        assert False, "Expected ValueError not raised"

def test_generate_code_post_request_invalid_field():
    """
    Test GenerateCodePostRequest with invalid field value
    """
    user = User(username="test_user", email="test_user@example.com")
    try:
        request = GenerateCodePostRequest(
            user=user,
            language="java",
            code_template="print('Hello {{ name }}!')",
            context={"name": "World"})
    except ValueError as e:
        assert str(e) == "Invalid field value: 'language'"
    else:
        assert False, "Expected ValueError not raised"

def test_generate_code_post_request_invalid_context():
    """
    Test GenerateCodePostRequest with invalid context
    """
    user = User(username="test_user", email="test_user@example.com")
    try:
        request = GenerateCodePostRequest(
            user=user,
            language="python",
            code_template="print('Hello {{ name }}!')",
            context={"name": 123})
    except ValueError as e:
        assert str(e) == "Invalid field value: 'context'"
    else:
        assert False, "Expected ValueError not raised"