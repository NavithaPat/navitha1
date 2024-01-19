a=str(input('enter your username'))
b=int(input('enter your password'))
d={'user name':'abcdef','password':'1234'}
if a in d['username']:
     print('successfully login')
elif b in d['password']:
     print('successfully login')
else:
     print('enter user number or correct password')