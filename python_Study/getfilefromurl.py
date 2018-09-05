from urllib import request
file = request.urlopen(r'http://helloworldbook.com/data/message.txt')
message = file.read()
print(message)
