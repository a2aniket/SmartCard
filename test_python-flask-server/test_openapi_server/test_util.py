from python-flask-server.openapi_server.util import *
def test_deserialize_primitive():
    assert _deserialize_primitive(1, int) == 1
    assert _deserialize_primitive(1.1, float) == 1.1
    assert _deserialize_primitive("hello", str) == "hello"
    assert _deserialize_primitive(True, bool) == True

def test_deserialize_object():
    assert _deserialize_object("test") == "test"
    assert _deserialize_object(123) == 123

def test_deserialize_date():
    assert deserialize_date(None) == None
    assert deserialize_date("2022-12-31") == datetime.date(2022, 12, 31)

def test_deserialize_datetime():
    assert deserialize_datetime(None) == None
    assert deserialize_datetime("2022-12-31T23:59:59.000Z") == datetime.datetime(2022, 12, 31, 23, 59, 59)

def test_deserialize_list():
    assert _deserialize_list([1,2,3], int) == [1,2,3]
    assert _deserialize_list(["a", "b", "c"], str) == ["a", "b", "c"]
    assert _deserialize_list([], int) == []

def test_deserialize_dict():
    assert _deserialize_dict({'a': 1, 'b': 2}, int) == {'a': 1, 'b': 2}
    assert _deserialize_dict({'a': 'hello', 'b': 'world'}, str) == {'a': 'hello', 'b': 'world'}
    assert _deserialize_dict({}, int) == {}

def test_deserialize_model():
    class TestModel:
        openapi_types = {"a": str, "b": int}
        attribute_map = {"a": "A", "b": "B"}

    model_data = {"A": "hello", "B": 123}
    instance = deserialize_model(model_data, TestModel)
    assert instance.a == "hello"
    assert instance.b == 123

def test_deserialize():
    assert _deserialize(None, int) == None
    assert _deserialize(123, int) == 123
    assert _deserialize("hello", str) == "hello"
    assert _deserialize(False, bool) == False
    assert _deserialize(datetime.date(2022, 12, 31), datetime.date) == datetime.date(2022, 12, 31)
    assert _deserialize(datetime.datetime(2022, 12, 31, 23, 59, 59), datetime.datetime) == datetime.datetime(2022, 12, 31, 23, 59, 59)
    assert _deserialize([1,2,3], typing.List[int]) == [1,2,3]
    assert _deserialize({'a': 1, 'b': 2}, typing.Dict[str, int]) == {'a': 1, 'b': 2}