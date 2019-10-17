import os
from flask import Flask, request, jsonify
from pprint import pprint
from dotenv import load_dotenv

app = Flask(__name__)

nexmo_number = "447520635498"
audio_url = "https://raw.githubusercontent.com/tbedford/git-testing-repo/master/tunes/Komiku_Sunset_on_the_beach.mp3"

if 'AUDIO_URL' in os.environ:
    audio_url = os.environ['AUDIO_URL']
    print("audio_url: %s" % audio_url)

if 'NEXMO_NUMBER' in os.environ:
    nexmo_number = os.environ['NEXMO_NUMBER']

ncco = [
    {
        "action": "stream",
        "loop": 0,
        "streamUrl": [audio_url]
    }
]
    
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
    app.run(host="localhost", port=9000)
