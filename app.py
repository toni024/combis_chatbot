#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @app.route('/<path:path>')
# def static_file(path):
#     return app.send_static_file(path)

from flask import Flask, send_from_directory, request
import json
import requests
import google_helpers
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


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


@app.route("/check", methods=['POST', 'GET'])
def check():
    # post data message, longitute, latitude
    if request.method == 'GET':
        return json.dumps({'text': 'hello'})
    else:
        data = request.data
        text = json.loads(data)['message']
        data = json.loads(data)
        data['longitude'] = '15'
        data['latitude'] = '45'
        text = text.encode('utf-8')
        log.debug("text read: "+text)

        
        # text = urllib.quote_plus(text)
        # log.debug("text after quote plus: "+text)

        english = google_helpers.translate_to_english(text)
        text = english.get("text")[0]

        # a = {'text': text, 'to': 'en'}
        
        # english = requests.get("http://www.transltr.org/api/translate?"+urllib.urlencode(a))
        # # #english =

        
        # english = english.json()
        #text = english.get("translationText")

        log.debug("enblish translation: " + text)
        datae = sendToBot(text)
        log.debug(json.dumps(datae))
        intent = getIntent(datae)
        if intent is None:
            return json.dumps({"text": "null"})

        # brute force FTW !
        if intent == "hospital":
            return google_helpers.fetch_google_places({
                'latitude': data['latitude'],
                'longitude': data['longitude'],
                'type': intent})
        elif intent == "food":
            return google_helpers.fetch_google_places({
                'latitude': data['latitude'],
                'longitude': data['longitude'],
                'type': 'restaurant'})
        elif intent == "drink":
            return google_helpers.fetch_google_places({
                'latitude': data['latitude'],
                'longitude': data['longitude'],
                'type': 'cafe'})
        elif intent == "nightlife":
            return google_helpers.fetch_google_places({
                'latitude': data['latitude'],
                'longitude': data['longitude'],
                'type': 'night_club'})
        elif intent == "accomodation":
            return google_helpers.fetch_google_places({
                'latitude': data['latitude'],
                'longitude': data['longitude'],
                'type': 'lodging'})
        elif intent == "siteseeing":
            return google_helpers.fetch_google_places({
                'latitude': data['latitude'],
                'longitude': data['longitude'],
                'type': 'museum|casino'})
        elif intent == "police":
            return google_helpers.fetch_google_places({
                'latitude': data['latitude'],
                'longitude': data['longitude'],
                'type': intent})
        elif intent == "atm":
            return google_helpers.fetch_google_places({
                'latitude': data['latitude'],
                'longitude': data['longitude'],
                'type': intent})
        elif intent == "greeting":
            return json.dumps({'text': 'hi'})
        elif intent == "weather":
            pass

        log.debug("intent retuned: " + intent)
        return json.dumps({'text': intent})


def getIntent(data):
    # print(datae)
    # print(datae.get("entities").get("intent")[0])
    # print(type(json.dumps({'text': datae.get("entities").get("intent")})))
    temp = data.get("entities").get("intent")
    if temp is None:
        log.debug("getIntent is None")
        return None
    else:
        log.debug("getIntent: " + json.dumps(temp))
        return temp[0].get("value")


def sendToBot(text):
    witToken = "XGCQNQXGXO6DMGQGPNMYJ2C4HZNKBF5Z"
    text = text.replace(" ", "+")
    header = {'Authorization': 'Bearer '+witToken}
    log.debug("text for bot {0}".format(text))
    return requests.get("https://api.wit.ai/message?v=20160526&q="+text,
                        headers=header).json()

log = None

if __name__ == '__main__':
    google_helpers.log = app.logger
    log = app.logger
    app.debug = debug
    app.run(host='0.0.0.0')
