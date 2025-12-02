import pytest
from flask import Flask
from src.flask_app import app  # import your Flask app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_addition(client):
    response = client.post("/calculate", json={"a": 5, "b": 3, "operation": "add"})
    assert response.status_code == 200
    assert response.get_json()["result"] == 8

def test_subtraction(client):
    response = client.post("/calculate", json={"a": 10, "b": 4, "operation": "sub"})
    assert response.status_code == 200
    assert response.get_json()["result"] == 6

def test_invalid_operation(client):
    response = client.post("/calculate", json={"a": 5, "b": 2, "operation": "mul"})
    assert response.status_code == 400  # or whatever you return for invalid ops