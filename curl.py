# -*- coding: utf-8 -*-

'''
分词测试
'''

import requests
import time

headers = {
    'Content-type': 'application/json'
}

data = {
    'segOrPos': 'seg',
    'useDict': 'no',
    'sentences': []
}

def curl():
    response = requests.post(url='http://172.16.13.117:8091/segPos', headers=headers, json=data)
    return response.json()

start = time.time()
response = []
with open('query.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line:
        data['sentences'].append(line)
        line = f.readline()

response = curl()
span = time.time() - start
print(span)
print(response)
with open('segResult.txt', 'w', encoding='utf-8') as f:
    for r in response:
        f.write(r + '\n')










