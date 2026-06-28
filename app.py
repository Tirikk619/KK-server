from flask import Flask, request, jsonify
from datetime import datetime
import requests
import os

app = Flask(__name__)

latest_data = {}

def get_weather():
    try:
        r = requests.get('https://wttr.in/合肥?format=j1', timeout=5)
        w = r.json()
        current = w['current_condition'][0]
        return {
            'temp_c': current['temp_C'],
            'feels_like_c': current['FeelsLikeC'],
            'humidity': current['humidity'],
            'desc': current['weatherDesc'][0]['value'],
            'wind_kmph': current['windspeedKmph'],
        }
    except:
        return {}

@app.route('/upload', methods=['POST'])
def upload():
    global latest_data
    latest_data = request.json or {}
    latest_data['received_at'] = datetime.now().isoformat()
    latest_data['weather'] = get_weather()
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

