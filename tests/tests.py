import os
from unittest.mock import patch

from dotenv import load_dotenv
from starlette.testclient import TestClient
from main import app

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")

client = TestClient(app)
auth_header = {"X-API-Key": API_KEY}


def test_read_main_authorized():
    response = client.get("/", headers=auth_header)
    assert response.status_code == 200
    assert response.json() == {"message": "Server is running."}


def test_read_main_not_authorized():
    response = client.get("/")
    assert response.status_code == 403
    assert response.json() == {"detail": "Not authenticated"}


@patch("currency_converter.CurrencyConverter.convert")
def test_convertion_authorized(mock_fn):
    mock_fn.return_value = 10.0
    response = client.get("/convert?convert_from=USD&convert_to=EUR&amount=100", headers=auth_header)
    assert response.status_code == 200
    response = response.json()
    assert response["convert_from"] == "USD"
    assert response["convert_to"] == "EUR"
    assert response["amount"] == 100.0
    assert response["converted_amount"] == 10


def test_convertion_not_authorized():
    response = client.get("/convert?convert_from=USD&convert_to=EUR&amount=100")
    assert response.status_code == 403
    assert response.json() == {"detail": "Not authenticated"}


def test_not_valid_currency():
    with patch("currency_converter.CurrencyConverter.convert", side_effect=ValueError("Not supported")):
        response = client.get("/convert?convert_from=USD&convert_to=EUR&amount=100", headers=auth_header)
        assert response.status_code == 404
        assert response.json() == {"message": "Not supported"}
