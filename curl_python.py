# -*- coding: utf-8 -*-
import requests
import time
import threading

requests

headers = {
    'Content-type': 'application/json'
}

data = {
    'segOrPos': 'seg',
    'useDict': 'yes',
    'sentences': ['今天天气真好，心情也很好！']
}

# start_time = time.time()
# for i in range(10):
#     response = requests.post(url='http://xxx.xxx.xxx.xxx:xxxx/segPos', headers=headers, json=data)
# span = time.time() - start_time
# print(span)

def curl():
    start_time = time.time()
    response = requests.post(url='http://xxx.xxx.xxx.xxx:xxxx/segPos', headers=headers, json=data)
    time_gap = time.time() - start_time
    print('thread %s use time %f s' %(threading.current_thread(), time_gap))
    # print(response.text)

def main():
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=curl))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()

