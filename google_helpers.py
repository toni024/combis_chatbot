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
def fetch_google_places(args1, latitude=None, longitude=None, content_type=None, keyword=None, radius='3000', location=None):
    args = args1
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
    if args.get('location'):
        location = args['location']
    api_key = 'AIzaSyB2T3V59a4UT2--vEUKw-KVI78lueAy9ds'
    if location:
        url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+location+'&key='+api_key
        response = requests.get(url).json()
        if response.get('results'):
            res_arr = response.get('results')
            latitude = res_arr[0].get('location').get('lat')
            longitude = res_arr[0].get('location').get('lon')
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
    response = requests.get(url).json()
    ret_arr = []
    if response.get('results'):
        res_arr = response.get('results')
        for res in res_arr:
            name = res.get('name')
            address = res.get('vicinity')
            if res.get('photos'):
                photo_ref = res.get('photos')[0].get('photo_reference')
                link = 'https://maps.googleapis.com/maps/api/place/photo?photoreference='+photo_ref+'&maxwidth=300&key='+api_key
                item = {
                    'name': name,
                    'address': address,
                    'link': link
                }
                ret_arr.append(item)
        return ret_arr
    return []


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


def translate_to_native(lan):
    sentence = "hi, i'm bot try something related to food, police, weather..."
    encoded_sentence = urllib.quote_plus(sentence)
    key = 'trnsl.1.1.20170408T140154Z.8efdaac6447952eb.3511edc0fcd5a38e5b92f9ec1a91266d894c1943'
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key='+key+'&lang=en-'+lan+'&text='+encoded_sentence
    response = requests.get(url)
    lang = response.json().get('lang')
    #url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key='+key+'&lang='+lang+'-en&text='+encoded_sentence
    response = requests.get(url)
    return response.json().get("text")[0]


def get_weather_forecast(args, latitude=None, longitude=None):
    icon_map = {
        "01d": "wi wi-day-sunny",
        "02d": "wi wi-day-cloudy",
        "03d": "wi wi-cloud",
        "04d": "wi wi-cloudy",
        "09d": "wi wi-rain",
        "10d": "wi wi-day-rain",
        "11d": "wi wi-thunderstorm",
        "13d": "wi wi-snow",
        "50d": "wi wi-fog",
        "01n": "wi wi-night-clear",
        "02n": "wi wi-night-alt-cloudy",
        "03n": "wi wi-cloud",
        "04n": "wi wi-cloudy",
        "09n": "wi wi-rain",
        "10n": "wi wi-night-alt-rain",
        "11n": "wi wi-thunderstorm",
        "13n": "wi wi-snow",
        "50n": "wi wi-fog",
    }
    json_args = args
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
            'description': day.get('weather')[0].get('main'),
            'link': 'http://openweathermap.org/img/w/'+day.get('weather')[0].get('icon')+'.png',
            'i': icon_map.get(day.get('weather')[0].get('icon'))
        }
        ret_arr.append(item)
    return ret_arr



if __name__ == "__main__":
    pass
    #args = sys.argv[1]
    #print(fetch_google_places('{"latitude":"45.815399","longitude":"15.966568","type":"restaurant","radius":"5000"}'))
    #print(translate_to_english("kakvo je vrijeme u splitu"))
#    a =
#    print(fetch_google_places('{"latitude":"15.2384","longitude":"45.1235234","type":"sightseeing"}'))
 #   print(fetch_google_places('{"latitude":"45.2384","longitude":"15.1235234","type":"restaurant"}'))
    print(get_weather_forecast({"latitude":"45.815399","longitude":"15.966568"}))
