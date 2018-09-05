#!/usr/bin/python3
# -*-coding:UTF-8-*-


class MyClass(object):
    i = 123

    def __init__(self, name):
        self.__name = name

    def f(self):
        return "hello," + self.__name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if len(new_name) > 5:
            print("please input name less than 5 characters")
        else:
            self.__name = new_name

use_class = MyClass('Lin')
print(use_class.get_name())
use_class.set_name("ZHUddd")
print(use_class.f())



