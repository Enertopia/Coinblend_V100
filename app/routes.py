from app import app
from .payment_processor import process_payment

@app.route('/')
def index():
    return "Welcome to Coinblend by BitcoinCab!"
