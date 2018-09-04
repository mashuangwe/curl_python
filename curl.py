'''
分词测试
'''

# -*- coding: utf-8 -*-

import requests
import time
import threading


headers = {
    'Content-type': 'application/json'
}

data = {
    'segOrPos': 'seg',
    'useDict': 'no',
    'sentences': ['今天天气真好，心情也很好！']
}

def curl():
    response = requests.post(url='http://172.16.13.117:8091/segPos', headers=headers, json=data)
    return response.text

response = curl()
print(response)


# if __name__ == '__main__':
#     main()










