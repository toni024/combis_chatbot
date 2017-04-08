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


def get_weather_forecast(args, latitude=None, longitude=None):
    icon_map = {
        "01d": "<i class=\"wi wi-day-sunny\"></i>",
        "02d": "<i class=\"wi wi-day-cloudy\"></i>",
        "03d": "<i class=\"wi wi-cloud\"></i>",
        "04d": "<i class=\"wi wi-cloudy\"></i>",
        "09d": "<i class=\"wi wi-rain\"></i>",
        "10d": "<i class=\"wi wi-day-rain\"></i>",
        "11d": "<i class=\"wi wi-thunderstorm\"></i>",
        "13d": "<i class=\"wi wi-snow\"></i>",
        "50d": "<i class=\"wi wi-fog\"></i>",
        "01n": "<i class=\"wi wi-night-clear\"></i>",
        "02n": "<i class=\"wi wi-night-alt-cloudy\"></i>",
        "03n": "<i class=\"wi wi-cloud\"></i>",
        "04n": "<i class=\"wi wi-cloudy\"></i>",
        "09n": "<i class=\"wi wi-rain\"></i>",
        "10n": "<i class=\"wi wi-night-alt-rain\"></i>",
        "11n": "<i class=\"wi wi-thunderstorm\"></i>",
        "13n": "<i class=\"wi wi-snow\"></i>",
        "50n": "<i class=\"wi wi-fog\"></i>",
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
    # print(get_weather_forecast('{"latitude":"45.815399","longitude":"15.966568"}'))
