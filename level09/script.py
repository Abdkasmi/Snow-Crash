string = enumerate(list(open('/home/user/level09/token', 'r'))[0].rstrip('\n'))
flag = ''.join([chr(ord(i) - c) for c, i in string])
print('flag : ' + flag + ' | with len ' + str(len(flag)))
