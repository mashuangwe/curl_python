# -*- coding: utf-8 -*-
import requests
import time
import threading

headers = {
    'Content-type': 'application/json'
}

data = {
    'segOrPos': 'seg',
    'useDict': 'yes',
    'sentences': ['今天天气真好', '带着理想前进', '开水房在哪']
}

# start_time = time.time()
# for i in range(10):
#     response = requests.post(url='http://xxx.xxx.xxx.xxx:xxxx/segPos', headers=headers, json=data)
# span = time.time() - start_time
# print(span)

def curl():
    start_time = time.time()
    response = requests.post(url='http://172.16.31.1:30380/segPos', headers=headers, json=data)
    time_gap = time.time() - start_time
    print(response.text)
    print('thread %s use time %f s' %(threading.current_thread(), time_gap))
    # print(response.text)


if __name__ == '__main__':
    curl()
