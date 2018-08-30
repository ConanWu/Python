#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def info(self):
         return 'hello'

# stu = Student('Lin', 100)
# stu.info()
# Student.info(stu)
stu = Student("Lin", 100)
stu.info()
