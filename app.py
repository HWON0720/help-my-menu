from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import key_reader
api_key = key_reader.get_api_key()

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)