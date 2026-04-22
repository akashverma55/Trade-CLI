import os
from binance.client import Client
from dotenv import load_dotenv

TESTNET_URL = "https://testnet.binance.vision/api"

def get_client():
    load_dotenv()

    api_key = os.getenv("API_KEY")
    secret_key = os.getenv("SECRET_KEY")

    if not api_key or not secret_key:
        raise ValueError("API_KEY or SECRET_KEY is missing")
    
    client = Client(api_key, secret_key)
    client.API_URL = TESTNET_URL

    return client