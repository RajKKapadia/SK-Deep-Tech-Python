import os

import requests
from dotenv import load_dotenv
load_dotenv()

TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')

BASE_URL = f'https://api.telegram.org/bot{TELEGRAM_API_KEY}'

def send_message(sender_id: int, text: str) -> None:
    url = f'{BASE_URL}/sendMessage'
    payload = {
        'chat_id': sender_id,
        'text': text
    }
    headers = {'Content-Type': 'application/json'}
    requests.request('GET', url, json=payload, headers=headers)
