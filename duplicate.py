b=input('helloworld')
out=''
for char in b:
    if char not in out:
        out+=char
print(out)