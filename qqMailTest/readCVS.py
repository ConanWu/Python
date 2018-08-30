import csv #import csv pakage

date = csv.reader(open('user_info.csv', 'r'))

for user in date:
    print(user)
    print(user[0])