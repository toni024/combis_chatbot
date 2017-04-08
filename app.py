# @app.route('/<path:path>')
# def static_file(path):
#     return app.send_static_file(path)

from flask import Flask, send_from_directory, request
import json
import requests
import logging


# app = Flask(__name__, static_url_path='/build')
app = Flask(__name__)
debug = True


# servers index page
@app.route('/')
def index():
    # header = {'Authorization': 'Bearer '+witToken}
    # req = requests.get("https://api.wit.ai/message?v=20160526&q=apartman",
    #                    headers=header)
    # return json.dumps(req.json())
    return send_from_directory('build/', 'index.html')


@app.route("/send/<text>", methods=['GET', 'POST'])
def senda(text):
    req = json.dumps(sendToBot(text).json())
    return req


witToken = "XGCQNQXGXO6DMGQGPNMYJ2C4HZNKBF5Z"


@app.route("/check", methods=['POST', 'GET'])
def check():
            # {"entities": {}, "msg_id": "53ebc318-bded-421c-85b3-6bb74a5b01ac", "_text": "bok"}
# 172.16.216.58 - - [08/Apr/2017 16:35:22] "POST /check HTTP/1.1" 200 -
# INFO:werkzeug:172.16.216.58 - - [08/Apr/2017 16:35:22] "POST /check HTTP/1.1" 200 -
# text read: kaj kurac
# {"entities": {"intent": [{"confidence": 0.5890985834213512, "value": "bezobraznik"}], "location": [{"suggested": true, "confidence": 0.9630074209263095, "type": "value", "value": "kaj kurac"}]}, "msg_id": "bd6a6a48-173a-48b7-9e97-71216d129691", "_text": "kaj kurac"}
    
    # post data message, longitute, latitude
    if request.method == 'GET':
        return json.dumps({'text': 'hello'})
    else:
        text = json.loads(request.data)
        print("text read: "+text['message'])
        #datae = json.dumps(sendToBot(text['message']))
        datae = sendToBot(text['message'])
        intent = getIntent(datae)
        
        print(datae)
        print(datae.get("entities").get("intent")[0])
        print(type(json.dumps({'text': datae.get("entities").get("intent")})))
        return json.dumps({'text': datae.get("entities").get("intent")[0]})



def getIntent(data):
    temp = datae.get("entities").get("intent")[0]


def sendToBot(text):
    text = text.replace(" ", "+")
    header = {'Authorization': 'Bearer '+witToken}
    logging.debug("text for bot {0}".format(text))
    return requests.get("https://api.wit.ai/message?v=20160526&q="+text,
                        headers=header).json()


if __name__ == '__main__':
    app.debug = debug
    app.run(host='0.0.0.0')
