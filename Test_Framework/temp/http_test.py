# !usr/bin/python3
# -*- coding:utf-8 -*-

import requests

r = requests.get(url='https://www.baidu.com', timeout=1)
print(r.status_code)
print(r)
r = requests.get(url='https://dict.baidu.com/s', params={'wd': 'python'})
print(r.url)
# print(r.text)
r = requests.post(url='http://httpbin.org/post', data={'key1': 'value1', 'key2': 'value2'})
print(r.url)
print(r.text)
# host = "http://httpbin.org/"
# endpoint = "post"
# url = ''.join([host, endpoint])
# data = {'key1': 'value1', 'key2': 'value2'}
#
# r = requests.post(url, data=data)
# #response = r.json()
# print(r.text)