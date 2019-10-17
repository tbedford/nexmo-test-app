import os
import sys
from flask import Flask, request, jsonify
from pprint import pprint
from dotenv import load_dotenv

# If running on Heroku the environment variables are set in Heroku when you click to deploy.

if 'AUDIO_URL' in os.environ:
    audio_url = os.environ['AUDIO_URL']
else:
    print("Set AUDIO_URL")
    sys.exit(-1) 

if 'NEXMO_NUMBER' in os.environ:
    nexmo_number = os.environ['NEXMO_NUMBER']
else:
    print("Set NEXMO_NUMBER")
    sys.exit(-1)

ncco = [
    {
        "action": "stream",
        "loop": 0,
        "streamUrl": [audio_url]
    }
]

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Call %s and listen to music...</p>" % nexmo_number

@app.route("/webhooks/answer")
def answer_call():
    params = request.args
    pprint(params)
    return jsonify(ncco)

@app.route("/webhooks/event", methods=['POST'])
def events():
    data = request.get_json()
    pprint(data)
    return ("200")

# For testing locally only
# Loads .env file from local drive and runs on port 9000
if __name__ == '__main__':
    print("Running locally")
    load_dotenv() 
    app.run(host="localhost", port=9000)
