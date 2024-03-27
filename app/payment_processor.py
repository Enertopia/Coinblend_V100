from flask import request, jsonify
from decimal import Decimal
import logging
from crypto_clients.bitcoin_client import BitcoinClient
from crypto_clients.ethereum_client import EthereumClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def convert_to_crypto(fiat_amount, crypto_choice):
    if crypto_choice == 'BTC':
        client = BitcoinClient()
    elif crypto_choice == 'ETH':
        client = EthereumClient()
    else:
        return None
    crypto_amount = fiat_amount * Decimal('0.05')  # 5% allocation
    return crypto_amount

@app.route('/process-payment', methods=['POST'])
def process_payment():
    data = request.get_json()
    fiat_amount = Decimal(data['fiat_amount'])
    crypto_choice = data.get('crypto_choice', 'BTC')
    crypto_amount = convert_to_crypto(fiat_amount, crypto_choice)
    logger.info(f"Processing {crypto_amount} of {crypto_choice} transaction")
    return jsonify({"status": "success", "message": "Payment processed successfully"}), 200
