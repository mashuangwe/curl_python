# -*- coding: utf-8 -*-
import requests, json
import time
import threading

headers = {
    'Content-type': 'application/json'
}

data = {
    'sentence': '于大宝的进球帮助中国队在长沙贺龙体育中心以1-0的比分获得胜利'
}

def curl():
    start_time = time.time()
    response = requests.post(url='http://172.16.23.6:2299', headers=headers, json=data)
    time_gap = time.time() - start_time
    print(response.text)
    print('thread %s use time %f s' %(threading.current_thread(), time_gap))

if __name__ == '__main__':
    curl()