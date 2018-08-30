#!/usr/bin/python3
# -*-coding:utf-8 -*-


n = 0
fields = ['a','b','c']
while n < len(fields):
    # print("当前数字是:",fields[n])
    n += 1


for i in 'fields':
    print("当前数字是:", i)
tups = {'name': 'xiaozhu', 'number': '1002'}
for i in tups:
    print(i, tups[i])

# 字典对象的循环
for key, value in tups.items():
    print(key, value)

# 并行迭代
for num1, num2 in zip(range(3), range(100)):
    print('zip的键值是：', num1, num2)

# 翻转和排序迭代reverse sort
a = ['1', '7', '4', '2']
print(sorted(a))
print(a)
print(sorted('hello,world!'))
print(list(reversed('hello,world!')))
print(''.join(reversed('hello,world!')))    # join 可以转化一个可迭代对象

# 跳出循环
for i in 'hello,world!':
    if i == 'o':
        break
    print(i)

for i in 'hello,world!':
    if i == 'o':
        continue
    print(i)

num = 10
while num > 0:
    print('num is :', num)
    num -= 1
    if num == 7:
        break
num = 10
while num > 0:
    if num == 7:
        num -= 1
        continue
    print('num2 is :', num)
    num -= 1
else:
    print('num is less than or equal 0, num is:', num)


# 99乘法表

tempStr = ''
for x in range(1, 10):
    for y in range(1, x + 1):
        # print(x, '*', y, '=', x*y)
        # tempStr = tempStr + str(x) + '*' + str(y) + '=' + str(x*y) + ' '
        print(str(x), '*', str(y), '=', str(x*y), '\t', end='')
    print('\n')

for i in range(1, 10):
        for j in range(1, i+1):
            print('{}x{}={}\t'.format(i, j, i*j), end='')
        print()

# print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))

for i in range(1, 10):
        for j in range(1, i+1):
            print('%dx%d=%d\t' %(i, j, i*j), end='')
        print()

# verify the number is odd number or an even number
user_input = int(input('please provide the number:'))
if user_input%2 == 0:
    print('the number :{} is even number'.format(user_input))
else:
    print('the number :{} is odd number!'.format(user_input))


# 检验一个数是否为阿姆斯特朗数
user_inputStr = input('please provide the number which you want to verify:')
user_inputNum = int(user_inputStr)
lenStr = len(user_inputStr)
calculateNum = 0
for i in range(lenStr):
    calculateNum += int(user_inputStr[i])**lenStr
print('calculateNum is :', calculateNum)
if calculateNum == user_inputNum:
    print('user input number :%d is Armstrong number!' % user_inputNum)
else:
    print('user input number: %d, is not Armstrong number! The calculatedNum is: %d' % (user_inputNum, calculateNum))






