#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @app.route('/<path:path>')
# def static_file(path):
#     return app.send_static_file(path)

from flask import Flask, send_from_directory, request
import re
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
        data['longitude'] = '15.966568'
        data['latitude'] = '45.815399'
        text = text.encode('utf-8')
        if text is None:
            return json.dumps({'text': 'Plz write something',
                               'google_maps': "null",
                               "weather": "null"})
        log.debug("text read: "+text)


        # text = urllib.quote_plus(text)
        # log.debug("text after quote plus: "+text)

        english = google_helpers.translate_to_english(text)
        nativeLang = english.get("lang").split("-")[0]  # TODO may fall
        #log.debug(english)
        text = english.get("text")[0]

        # a = {'text': text, 'to': 'en'}
        
        # english = requests.get("http://www.transltr.org/api/translate?"+urllib.urlencode(a))
        # # #english =

        
        # english = english.json()
        #text = english.get("translationText")

        log.debug("enblish translation: " + text)
        datae = sendToBot(text)
        # log.debug(datae)
        daysNumber = getNumber(datae)
        intent = getIntent(datae)
        place = getPlace(datae)
        log.debug("intent: {0}    place: {1}    number: {2}".format(intent,
                                                                    place,
                                                                    daysNumber))
        if intent is None:
            return json.dumps({"text": "Error"})

        # brute force FTW !
        if intent == "hospital":
            t = {'text': 'null',
                 'weather': 'null',
                 'google_maps': google_helpers.fetch_google_places({
                     'latitude': data['latitude'],
                     'longitude': data['longitude'],
                     'location': place,
                     'type': intent})}
            return json.dumps(t)
        elif intent == "food":
            t = {'text': 'null',
                 'weather': 'null',
                 'google_maps': google_helpers.fetch_google_places({
                     'latitude': data['latitude'],
                     'longitude': data['longitude'],
                     'location': place,
                     'type': 'restaurant'})}
            return json.dumps(t)
        elif intent == "drink":
            t = {'text': 'null',
                 'weather': 'null',
                 'google_maps': google_helpers.fetch_google_places({
                     'latitude': data['latitude'],
                     'longitude': data['longitude'],
                     'location': place,
                     'type': 'cafe'})}
            return json.dumps(t)
        elif intent == "nightlife":
            t = {'text': 'null',
                 'weather': 'null',
                 'google_maps': google_helpers.fetch_google_places({
                     'latitude': data['latitude'],
                     'longitude': data['longitude'],
                     'location': place,
                     'type': 'night_club'})}
            return json.dumps(t)
        elif intent == "accommodation":
            t = {'text': 'null',
                 'weather': 'null',
                 'google_maps': google_helpers.fetch_google_places({
                     'latitude': data['latitude'],
                     'longitude': data['longitude'],
                     'location': place,
                     'type': 'lodging'})}
            return json.dumps(t)
        elif intent == "siteseeing":
            t = {'text': 'null',
                 'weather': 'null',
                 'google_maps': google_helpers.fetch_google_places({
                     'latitude': data['latitude'],
                     'longitude': data['longitude'],
                     'location': place,
                     'type': 'museum|casino'})}
            return json.dumps(t)
        elif intent == "police":
            t = {'text': 'null',
                 'weather': 'null',
                 'google_maps': google_helpers.fetch_google_places({
                     'latitude': data['latitude'],
                     'longitude': data['longitude'],
                     'location': place,
                     'type': intent})}
            return json.dumps(t)
        elif intent == "atm":
            t = {'text': 'null',
                 'weather': 'null',
                 'google_maps': google_helpers.fetch_google_places({
                     'latitude': data['latitude'],
                     'longitude': data['longitude'],
                     'location': place,
                     'type': intent})}
            return json.dumps(t)
        elif intent == "greeting":
            return json.dumps({"text": google_helpers.translate_to_native(nativeLang),
                               "google_maps": "null",
                               "weather": "null"})
        elif intent == "weather":
            w = {"text": "null",
                 "google_maps": "null",
                 "weather": google_helpers.get_weather_forecast({
                     'location': place,
                     'days': daysNumber,
                     'latitude': data['latitude'],
                     'longitude': data['longitude']})}
            return json.dumps(w)

        log.debug("intent retuned: " + intent)
        return json.dumps({'text': intent})


def getPlace(data):
    temp = data.get("entities").get("location")
    if temp is None:
        log.debug("getIntent is None")
        return None
    else:
        log.debug("getIntent: " + json.dumps(temp))
        return temp[0].get("value")


def getNumber(data):
    log.debug(data)

    temp = data.get("entities").get("number")
    if temp is None:
        temp = data.get("_text")
        log.debug(temp)
        if temp is None:
            return None
        else:
            temp.split(" ")[3]
    log.debug(temp)
    if temp is None:
        # log.debug("getIntent is None")
        return None
    else:
        # log.debug("getIntent: " + json.dumps(temp))
        return temp[0].get("value")
    

def getIntent(data):
    # print(datae)
    # print(datae.get("entities").get("intent")[0])
    # print(type(json.dumps({'text': datae.get("entities").get("intent")})))
    temp = data.get("entities").get("intent")
    if temp is None:
        # log.debug("getIntent is None")
        return None
    else:
        # log.debug("getIntent: " + json.dumps(temp))
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
