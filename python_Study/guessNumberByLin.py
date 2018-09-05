# !/usr/bin/python3
# -*- coding:UTF-8 -*-

import random

number = random.randint(1, 100)
guess = 0

while True:
    num_input = input("please input a number between 0 and 100:")
    guess += 1
    if guess > 5:
        print('you already guess 5 times, you failed. please retry next time.')
    else:
        if not num_input.isdigit():
            print("please input a number!")
        elif int(num_input) < 0 or int(num_input) > 100:
            print('please input the number between 0 and 100!')
        else:
            num_input = int(num_input)
            if num_input == number:
                print('you got it, the number is: ', number)
            elif num_input < number:
                print('your guess number is too low, please re-input!')
            else:
                print('your guess number is too high, please re-input!')
