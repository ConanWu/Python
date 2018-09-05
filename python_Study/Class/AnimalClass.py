#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Animal(object):
    def run(self):
        print("Animal is running!")

    def __run(self):
        print("Private animal is running!")

    def jump(self):
        print("Animal is jumpping!")

class Dog(Animal):
    def run(self):
        print("Dog is running!")

class Cat(Animal):
    def run(self):
        print("Cat is running!")

dog = Dog()
dog.run()
dog.jump()
a = list()
b = Dog()
c = Animal()

print(isinstance(a, list))
print(isinstance(b, Dog))
print(isinstance(c, object))


def run_two_times(animal1):
    animal1.run()
    animal1.run()

run_two_times(Animal())
run_two_times(Dog())
