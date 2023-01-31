import json
from flask import Flask, request, jsonify

app = Flask(__name__)


# serve index page
@app.route('/')
def serve_index():
    return "hello world"


# receive log-in info from user
@app.route('/login', methods=['POST'])
def login():
    info = json.loads(request.data)
    username = info.get('username')
    password = info.get('password')
    # do stuff