from flask import Flask, request, jsonify
from datetime import datetime
import requests
import os

app = Flask(__name__)

# 存储最新的传感器数据
latest_data = {}

@app.route('/upload', methods=['POST'])
def upload():
    global latest_data
    latest_data = request.json or {}
    latest_data['received_at'] = datetime.now().isoformat()
    return jsonify({"status": "ok"})

@app.route('/status', methods=['GET'])
def status():
    return jsonify(latest_data)

@app.route('/', methods=['GET'])
def home():
    return "kk-server is running"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
