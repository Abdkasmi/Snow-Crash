str = list(open('token', 'r'))[0]
flag = ''.join([chr(ord(i) - str.find(i)) for i in str])
