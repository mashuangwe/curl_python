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


# app_id=2108095633&nonce_str=0l82w4dxv1icpaof5tks&question=%E5%BA%8A%E5%89%8D%E6%98%8E%E6%9C%88%E5%85%89&session=10000&time_stamp=1535541160&app_key=YjC8YiifM7f3ysvJ
# app_id=2108095633&nonce_str=0l82w4dxv1icpaof5tks&question=%E5%BA%8A%E5%89%8D%E6%98%8E%E6%9C%88%E5%85%89&session=10000&time_stamp=1535541160&app_key=YjC8YiifM7f3ysvJ
#
# 2C40414714955A32D7DD727CC2F10BB4
# 2C40414714955A32D7DD727CC2F10BB4

# {"app_id":"2108095633","nonce_str":"0l82w4dxv1icpaof5tks","question":"床前明月光","session":"10000","time_stamp":"1535556835","sign":"801A4F486F96E5181B3143D8BB01CBFC"}
# {'time_stamp': '1535555810', 'question': '床前明月光', 'app_id': 2108095633, 'nonce_str': '0l82w4dxv1icpaof5tks', 'session': '10000', 'sign': 'CF0125E537974355112259D986EC3165'}
# {"app_id":"2108095633","nonce_str":"0l82w4dxv1icpaof5tks","question":"床前明月光","session":"10000","time_stamp":"1535555810",       "sign": "CF0125E537974355112259D986EC3165"}
#
#
# %E5%BA%8A%E5%89%8D%E6%98%8E%E6%9C%88%E5%85%89
# %E5%BA%8A%E5%89%8D%E6%98%8E%E6%9C%88%E5%85%89








