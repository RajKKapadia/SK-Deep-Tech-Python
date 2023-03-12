import json

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'ALL IS WELL...'

@app.route('/telegram', methods=['GET', 'POST'])
def telegram():
    body = request.get_json()
    print(json.dumps(body))
    return 'OK'
