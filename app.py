from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_data = {
        'name': request.form['name'],
        'email': request.form['email']
    }
    response = requests.post('http://127.0.0.1:5000/receive_data', json=user_data)
    if response.ok:
        return redirect(url_for('home'))
    else:
        return 'Failed to send data', 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
