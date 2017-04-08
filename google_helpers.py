#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import requests
import sys
import json
import urllib

log = logging.getLogger('test.log')

# input json example:
# fetch_google_places('{"latitude":"45.815399","longitude":"15.966568","type":"restaurant","radius":"5000"}')
# output json
def fetch_google_places(args1, latitude=None, longitude=None, content_type=None, keyword=None, radius='3000'):
    args = json.loads(args1)
    if args.get('latitude'):
        latitude = args['latitude']
    if args.get('longitude'):
        longitude = args['longitude']
    if args.get('radius'):
        radius = args['radius']
    if args.get('type'):
        content_type = args['type']
    if args.get('keyword'):
        keyword = args['keyword']
    api_key = 'AIzaSyB2T3V59a4UT2--vEUKw-KVI78lueAy9ds'
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
    if latitude and longitude and latitude != ''and longitude != '':
        url += 'location='+latitude+','+longitude
    if radius and radius != '':
        url += '&radius=' + radius
    if content_type and content_type != '':
        url += '&type='+content_type
    if keyword and keyword != '':
        url += '&keyword='+keyword
    url += '&key='+api_key
    response = requests.get(url)
    return response.json()


# input string example:
# translate_to_english("kakvo je vrijeme u splitu")
# output json exapmle:
# {u'lang': u'hr-en', u'text': [u'weather in split'], u'code': 200}
def translate_to_english(sentence):
    encoded_sentence = urllib.quote_plus(sentence)
    key = 'trnsl.1.1.20170408T140154Z.8efdaac6447952eb.3511edc0fcd5a38e5b92f9ec1a91266d894c1943'
    url = 'https://translate.yandex.net/api/v1.5/tr.json/detect?key='+key+'&text='+encoded_sentence+'&hint=sr,hr,bs,mk,bg,el,sl'
    response = requests.get(url)
    lang = response.json().get('lang')
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key='+key+'&lang='+lang+'-en&text='+encoded_sentence
    response = requests.get(url)
    return response.json()


def translate_to_base_lang(sentence, lang):
    encoded_sentence = urllib.quote_plus(sentence)
    key = 'trnsl.1.1.20170408T140154Z.8efdaac6447952eb.3511edc0fcd5a38e5b92f9ec1a91266d894c1943'
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key=' + key + '&lang=en-'+lang+'&text=' + encoded_sentence
    response = requests.get(url)
    log.info('test')
    return response.json()


def get_weather_forecast(args, latitude=None, longitude=None):
    json_args = json.loads(args)
    if json_args.get('latitude'):
        latitude = json_args['latitude']
    if json_args.get('longitude'):
        longitude = json_args['longitude']
    key = '71db68a35d054e9190cace3261ddfb97'
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?lat='+latitude+'&lon='+longitude+'&APPID='+key
    response = requests.get(url)
    forecast = response.json().get('list')
    ret_arr = []
    for day in forecast:
        item = {
            'temp': round(day.get('temp').get('day') - 273.15),
            'description': day.get('weather')[0].get('main')
        }
        ret_arr.append(item)
    return ret_arr


if __name__ == "__main__":
    #args = sys.argv[1]
    print(fetch_google_places('{"latitude":"45.815399","longitude":"15.966568","type":"sightseeing"}'))
    #print(translate_to_english("đe kafana"))
    #print(get_weather_forecast('{"latitude":"45.815399","longitude":"15.966568"}'))
    #print(translate_to_base_lang("we are in the very hell of a position", "hr"))