from flask import Flask, request, jsonify
from pprint import pprint

app = Flask(__name__)

audio_url = "https://raw.githubusercontent.com/tbedford/git-testing-repo/master/tunes/Komiku_Sunset_on_the_beach.mp3"

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
    return "<p>Call +44-(0)7520635498 and listen to music...</p>"

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

@app.route('/webhooks/inbound', methods=['POST'])
def inbound_message():
    print ("** inbound_message **")
    data = request.get_json()
    pprint(data)
    return ("inbound_message", 200)

@app.route('/webhooks/status', methods=['POST'])
def message_status():
    print ("** message_status **")
    data = request.get_json()
    pprint(data)
    return ("message_status", 200)

@app.route('/webhooks/inbound-sms', methods=['POST'])
def inbound_sms():
    print ("** inbound_sms **")
    values = request.values
    pprint(values)
    return ("inbound_sms", 200)

@app.route('/webhooks/delivery-receipt', methods=['POST'])
def delivery_receipt():
    print ("** delivery_receipt **")
    data = request.get_json()
    pprint(data)
    return ("delivery_receipt", 200)

if __name__ == '__main__':
    app.run(host="localhost", port=9000)
