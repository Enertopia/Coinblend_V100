import os

class Config:
    BTC_API_URL = os.getenv("BTC_API_URL")
    ETH_API_URL = os.getenv("ETH_API_URL")
    FIAT_API_URL = os.getenv("FIAT_API_URL")
    BTC_API_KEY = os.getenv("BTC_API_KEY")
    ETH_API_KEY = os.getenv("ETH_API_KEY")
    FIAT_API_KEY = os.getenv("FIAT_API_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
