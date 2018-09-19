# -*- coding: utf-8 -*-
import requests
import time
import urllib
import hashlib
import random

alphabet = []
for i in range(26):
    alphabet.append(chr(ord('a') + i))
for i in range(10):
    alphabet.append(str(i))

print(alphabet)
# print(''.join(random.sample(alphabet, 20)))

params = {
    'app_id': 2108095633,
    'session': '10000',
    'time_stamp': str(int(time.time())),
    'question': '床前明月光',
    'nonce_str': '0l82w4dxv1icpaof5tks', # ''.join(random.sample(alphabet, 20)),
    'sign': ''
}

appkey = 'YjC8YiifM7f3ysvJ'

def getReqSign(params, appkey):
    sortedParams = sorted(params.items(), key=lambda d: d[0])
    ss = ''
    for k, v in sortedParams:
        if v != '':
            ss += urllib.parse.urlencode({k : v}) + '&'
    ss += 'app_key=' + appkey

    print(ss)
    sign = hashlib.md5(ss.encode("utf-8"))
    sign = str.upper(sign.hexdigest())
    print(sign)
    return sign

params['sign'] = getReqSign(params, appkey)
print(params)

def curl():
    chat = requests.post(url='https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat', data=params)
    print(chat.text)

curl()







