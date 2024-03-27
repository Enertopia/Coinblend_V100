import requests
from config import Config

class CryptoClient:
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def get_real_time_price(self, symbol):
        response = requests.get(f"{self.api_url}/assets/{symbol}/", headers={'Authorization': f'Bearer {self.api_key}'})
        if response.status_code == 200:
            return response.json()['data']['priceUsd']
        else:
            return None
