import os

from flask import Flask, request
from dotenv import load_dotenv
load_dotenv()

from helper.telegram_api import send_message
from helper.openai_api import text_completion

app = Flask(__name__)

HEADER_TOKEN = os.getenv('HEADER_TOKEN')

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'ALL IS WELL...'

@app.route('/telegram', methods=['GET', 'POST'])
def telegram():
    try:
        body = request.get_json()
        message = body['message']
        chat = message['chat']
        sender_id = chat['id']
        text = message['text']
        secret_token = request.headers['X-Telegram-Bot-Api-Secret-Token']

        if HEADER_TOKEN == secret_token:
            print('Authenticated request.')

        '''
        We need to pass this incoming message to Openai
        Receive the response from Openai
        Send back a reponse to the request
        '''

        response = text_completion(text)

        send_message(sender_id, response)
    except:
        pass
    finally:
        return 'OK'
