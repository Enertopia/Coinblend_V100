from .crypto_client import CryptoClient
from config import Config

class EthereumClient(CryptoClient):
    def __init__(self):
        super().__init__(Config.ETH_API_URL, Config.ETH_API_KEY)
