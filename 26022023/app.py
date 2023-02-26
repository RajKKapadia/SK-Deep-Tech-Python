from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/contactus', methods=['GET', 'POST'])
def constact_us():
    return render_template('contactus.html')

if __name__ == '__main__':
    app.run(debug=True)
