import os
import json

import requests
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def text_completion(prompt: str) -> None:
    url = 'https://api.openai.com/v1/completions'
    payload = {
        'model': 'text-davinci-003',
        'prompt': f'Human: {prompt}\nAI: ',
        'max_tokens': 1000,
        'stop': ['Human: ', 'AI: ']
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}'
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    response = json.loads(response.text)
    text = response['choices'][0]['text']
    text = text.strip()
    
    return text
    