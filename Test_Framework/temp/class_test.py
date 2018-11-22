# !/usr/bin/python3
# -*- coding:utf-8 -*-


class people3:
    country = "china"

    @staticmethod
    def getCountry():
        return people3.country


p = people3()
print(p.getCountry())  # 实例对象调用类方法
print(people3.getCountry())  # 类对象调用类方法

