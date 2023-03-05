from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return jsonify(
        {
            'message': 'Success.'
        }
    )


@app.route('/api/get/users', methods=['GET', 'POST'])
def get_users():
    return jsonify(
        [
            {
                'name': "Rajesh",
                'email': 'rajesh@gmail.com'
            },
             {
                'name': "Mahesh",
                'email': 'mahesh@gmail.com'
            }
        ]
    )

@app.route('/api/get/user', methods=['GET', 'POST'])
def get_user():
    data = request.get_json()
    email = data['email']
    print(email)
    '''
    We connect to our database
    We check for the email in our database
    If email is there we send email information
    or we say no email found...
    '''
    return jsonify(
        [
            {
                'name': "Rajesh",
                'email': 'rajesh@gmail.com'
            },
             {
                'name': "Mahesh",
                'email': 'mahesh@gmail.com'
            }
        ]
    )
