# -*- coding: utf-8 -*-
import requests

params1 = {
    'email': 'johnny.fu@cloudminds.com',
    'token': '5782f094f164de040706b14f8a66ec4d419fea3e',
    'tag': '',
    'tsession': 'johnny.fu@fun_fun'
}

# params2 = {
#     'email': 'johnny.fu@cloudminds.com',
#     'token': '5782f094f164de040706b14f8a66ec4d419fea3e',
#     'said': '今天天氣如何',
#     'reply': ''
# }

# question = '巴赫'
question = '今天天氣如何'

params1['tag'] = question
print(params1)
def curl():
    chat1 = requests.post(url='https://jerry.ap-mic.com/apidisplay/8QQXJWE/', data=params1)
    print(chat1.json(), '\n')
    print(chat1.json()['reply'][0]['answer'])
curl()






