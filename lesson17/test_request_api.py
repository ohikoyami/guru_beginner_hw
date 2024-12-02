import json

import requests
from jsonschema import validate

BASE_URL = "https://reqres.in/api"


def test_post_create_user_positive():
    payload = {"name": "Daria", "job": "QA"}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Daria"


def test_put_update_user_info():
    payload = {"name": "Daria", "job": "developer"}
    response = requests.put(f"{BASE_URL}/users/2", json=payload)
    assert response.status_code == 200
    assert response.json()["job"] == "developer"


def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/2")
    assert response.status_code == 204


def test_post_create_user_negative():
    payload = {"email": "sydney@fife"}
    response = requests.post(f"{BASE_URL}/register", json=payload)
    assert response.status_code == 400


def test_user_not_founded():
    response = requests.get(f"{BASE_URL}/users/23")
    assert response.status_code == 404


def test_get_user_schema_with_response():
    response = requests.get(f"{BASE_URL}/users/2")
    json_response = response.json()
    with open('schemas/get_user.json') as file:
        validate(json_response, schema=json.loads(file.read()))


def test_login_user_successful_schema_with_response():
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/login", json=payload)
    json_response = response.json()
    with open('schemas/login_successful.json') as file:
        validate(json_response, schema=json.loads(file.read()))


def test_create_user_schema_with_response():
    payload = {"name": "Daria", "job": "QA"}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    json_response = response.json()
    with open('schemas/create_user.json') as file:
        validate(json_response, schema=json.loads(file.read()))


def test_update_user_schema_with_response():
    payload = {"name": "Daria", "job": "QA"}
    response = requests.put(f"{BASE_URL}/users/2", json=payload)
    json_response = response.json()
    with open('schemas/update_user.json') as file:
        validate(json_response, schema=json.loads(file.read()))


def test_delete_user_no_response():
    response = requests.delete(f"{BASE_URL}/users/2")
    assert response.status_code == 204
    assert response.text == ""


def test_create_user_response_business_logic():
    payload = {"name": "Daria", "job": "QA"}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    json_response = response.json()
    assert json_response.get('name') == payload['name']
    assert json_response.get('job') == payload['job']
