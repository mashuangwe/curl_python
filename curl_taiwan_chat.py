# -*- coding: utf-8 -*-
import requests

headers = {
    'Content-type': 'application/json',
    'neo-token': 'd3d3Ljk0Ym90LmNvbQ=='
}

data = {
  "question": "你家在台北市松山區什麼位置"
}

url = 'https://www.94bot.com/neo-restful/bot/getAnswer'

def curl():
    response = requests.post(url=url, headers=headers, json=data)
    print(response.text)

if __name__ == '__main__':
    curl()
