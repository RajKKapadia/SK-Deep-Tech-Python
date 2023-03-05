from flask import Flask, jsonify, request

from database.mongo_connection import create_mongo_user, get_mongo_user, update_mongo_user

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return jsonify(
        {
            'message': 'Success.'
        }
    )


@app.route('/api/create/user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'GET':
        return jsonify(
            {
                'message': 'GET method is not allowed for this route.'
            }
        )
    data = request.get_json()
    result = create_mongo_user(data)

    if result:
        return jsonify(
            {
                'message': 'User created successfully.'
            }
        )
    else:
        return jsonify(
            {
                'message': 'User not created.'
            }
        )


@app.route('/api/get/user', methods=['GET', 'POST'])
def get_user():
    if request.method == 'POST':
        return jsonify(
            {
                'message': 'POST method is not allowed for this route.'
            }
        )
    data = request.get_json()

    user = get_mongo_user(data['email'])

    if user == None:
        return jsonify(
            {
                'message': 'User not found.',
                'user': None
            }
        )
    else:
        return jsonify(
            {
                'message': 'User found',
                'user': user
            }
        )
    
@app.route('/api/update/user', methods=['GET', 'POST'])
def update_user():
    if request.method == 'GET':
        return jsonify(
            {
                'message': 'GET method is not allowed for this route.'
            }
        )
    data = request.get_json()

    user = update_mongo_user(data['email'], data['update'])

    if user == None:
        return jsonify(
            {
                'message': 'User not found.'
            }
        )
    else:
        return jsonify(
            {
                'message': 'User updated'
            }
        )
