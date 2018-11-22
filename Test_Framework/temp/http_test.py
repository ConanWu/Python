# !usr/bin/python3
# -*- coding:utf-8 -*-

import requests

r = requests.get(url='https://www.baidu.com', timeout=0.1)
print(r.status_code)
r = requests.get(url='https://dict.baidu.com/s', params={'wd': 'python'})
print(r.url)
# print(r.text)
r = requests.post(url='http://httpbin.org/', data={'key1': 'value1', 'key2': 'value2'})
print(r.url)
print(r.text)