rows=int(input('enter number for rows:-'))
n=rows//2
out=''
for i in range(rows):
    for j in range(rows):
        if i==n or j==n:
            out+=' '
        else:
            out+='* '
    out+='\n'
print(out)
