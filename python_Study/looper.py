import time
for i in range(10,0,-1):
    print(i)
    #time.sleep(1)
print("BLASH OFF!")

##someinput = input()
##while someinput == '3':
##    print("pass")
##    someinput = input()
##print("not 3")
a=input("which multiplaction table would you like?")
print("Here's your table:")
for i in range(1,11):
    print(a,"X",i,'=',int(a)*i)
j = 1
while j<11:
    print(a,'X',j,'=',int(a)*j)
    j+=1
