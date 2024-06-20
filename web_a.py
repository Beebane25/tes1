from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# Fungsi untuk membaca data dari file JSON
def load_data():
    if os.path.exists('data.json'):
        with open('data.json', 'r') as f:
            return json.load(f)
    else:
        return []

# Fungsi untuk menyimpan data ke file JSON
def save_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.get_json()

    # Memuat data yang sudah ada dari file JSON
    existing_data = load_data()

    # Pastikan existing_data adalah list
    if not isinstance(existing_data, list):
        existing_data = []

    # Menambahkan data baru ke dalam daftar
    existing_data.append(data)

    # Menyimpan data yang diperbarui ke file JSON
    save_data(existing_data)

    return jsonify({'status': 'success', 'message': 'Data received successfully'})

@app.route('/show_data')
def show_data():
    # Memuat data dari file JSON
    data = load_data()

    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
