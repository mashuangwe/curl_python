# -*- coding: utf-8 -*-
import requests
import time

headers = {
    'Content-type': 'application/json'
}

beijing = {
    'city' : 'CN101010100',
    'key' : 'c6eab390cb6d4fa0a9345ff63db30bef'
}

london = {
    'city' : 'GB2643741',
    'key' : 'c6eab390cb6d4fa0a9345ff63db30bef'
}

def curl():
    weather = requests.get(url='https://free-api.heweather.com/v5/weather', params=beijing)
    for w in weather:
        print(w)

    print('\n')
    weather = requests.get(url='https://free-api.heweather.com/v5/weather', params=london)
    for w in weather:
        print(w)


curl()










