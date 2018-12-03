# !usr/bin/python3
# -*- coding:utf-8 -*-


import requests,re

# 用户名和密码
username = '457907449@qq.com'
password = 'MH20110712'

# 新建一个session对象
s = requests.Session()

headerss = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
        }
# 首先访问一遍，得到BAIDUID
print("first geting \'www.baidu.com\'".center(40,'#'))
first_get = s.get("http://www.baidu.com",headers=headerss,)

print("current' cookies is:   ".center(40,'#'))
print(s.cookies.get_dict())
print("-"*40)
# 用BAIDUID访问包含token的地址，然后正则解析出token
print("now is ready to get token".center(40, '#'))
token_url = "https://passport.baidu.com/v2/api/?getapi&tpl=pp&apiver=v3&class=login"
token_data = re.findall(r'(?<=token" : ")[0-9a-z]+",', s.get(token_url, headers=headerss,).content)[0][:-2]
print("token is {}".format(token_data)+'\n'+"current's cookies is:\n{}".format(s.cookies.get_dict()))

print("-"*40)
# 现在post登陆信息，但是没有验证，只知道返回了BDUSS这条cookie
raw_post = {
    "username":username,
    "password":password,
    'u': 'https://passport.baidu.com/',
    'tpl': 'pp',
    "token": token_data,
    'staticpage': 'https://passport.baidu.com/static/passpc-account/html/v3Jump.html',
    'isPhone': 'false',
    'charset': 'UTF-8',
    'callback': 'parent.bd__pcbs__ra48vi'}
print("is posting baidu ".center(40,'#'))
# 这里折腾了好久，登陆地址用“https://passport.baidu.com/v2/?login”是错的，得不到BDUSS
pp = s.post("https://passport.baidu.com/v2/api/?login", headers=headerss, data=raw_post)
print("the cookies after post is:\n{}".format(s.cookies.get_dict()))
# 拿贴吧测试是否登录，返回页面不再是公共的了
txt = s.get("http://tieba.baidu.com/").content
print(txt)
with open("e:/a.html", 'wb') as f:
    f.write(txt)
    f.close()
