st=input('')
out={}
for char in st:
    if not(char in out):
        out[char]=1
    else:
        out[char]+=1
print(out)
