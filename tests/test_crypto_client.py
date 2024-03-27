import pytest
from crypto_clients.crypto_client import CryptoClient

@pytest.fixture
def crypto_client():
    return CryptoClient(api_url="https://fake-api.com", api_key="testkey")

def test_get_real_time_price(crypto_client):
    # Mock the API call within CryptoClient
    # Use requests_mock or a similar library to simulate API responses
    # Assert based on the mocked response
    assert crypto_client.get_real_time_price("BTC") == "Expected Price"
