import os
import sys
from flask import Flask, request, jsonify
from pprint import pprint
from dotenv import load_dotenv

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

if __name__ == '__main__':
    load_dotenv()
    if 'AUDIO_URL' in os.environ:
        audio_url = os.environ['AUDIO_URL']
    else:
        print("Create a .env file and add AUDIO_URL")
        sys.exit(-1)

    if 'NEXMO_NUMBER' in os.environ:
        nexmo_number = os.environ['NEXMO_NUMBER']
    else:
        print("Create a .env file and add NEXMO_NUMBER")
        sys.exit(-1)
    app.run(host="localhost", port=9000)
