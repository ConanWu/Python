# !usr/bin/python3
# -*- coding:utf-8 -*-

import requests
import json
# r = requests.get(url='https://www.baidu.com', timeout=1)
# print(r.status_code)
# print(r)
# r = requests.get(url='https://dict.baidu.com/s', params={'wd': 'python'})
# print(r.url)
# # print(r.text)
# r = requests.post(url='http://httpbin.org/post', data={'key1': 'value1', 'key2': 'value2'})
# print(r.url)
# print(r.text)
# print(r.content)
# host = "http://httpbin.org/"
# endpoint = "post"
# url = ''.join([host, endpoint])
# data = {'key1': 'value1', 'key2': 'value2'}
#
# r = requests.post(url, data=data)
# #response = r.json()
# print(r.text)
# r = requests.get('https://github.com/timeline.json', stream=True)
# print(r.raw)
# print(r.raw.read(500))

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
payload2 = (('key1', 'value2'), ('key2', 'value2'))
headers = {'User-Agent': 'Mozilla/5.0'}
r_get = requests.get("http://httpbin.org/get", params=payload)
r_post = requests.post("http://httpbin.org/post", data=payload)
r_post2 = requests.post("http://httpbin.org/post", data=payload2)
r_json = requests.get('https://github.com/timeline.json', stream=True)
r_baidu = requests.get('https://www.baidu.com', headers=headers)
# print(r_json.url)
# print(r_json.text)
# print(r_post.json())
print(r_post.url)
# print(r_post.text)
print(r_post.status_code)
print(r_post2.url)
# print(r_post2.text)
# r_post_string = requests.post('http://httpbin.org/post', data=json.dumps(payload))
# r_post_json = requests.post('http://httpbin.org/post', json=payload)
# print(r_post_string.text)
# print(r_post_json.text)
r = requests.head('http://github.com', allow_redirects=False)
print(r.url)
print(r.status_code)
print(r.history)

s = requests.session()
# s.auth('user', 'pass')
s.headers.update({'x-text': 'true'})
r_session = s.get('http://httpbin.org/headers', headers={'x-text2': 'true'})
print(r_session.text)
r_session2 = s.get('http://httpbin.org/headers')
print(r_session2.text)



