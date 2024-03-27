from .crypto_client import CryptoClient
from config import Config

class BitcoinClient(CryptoClient):
    def __init__(self):
        super().__init__(Config.BTC_API_URL, Config.BTC_API_KEY)
