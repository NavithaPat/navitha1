file=open(r"C:\Users\Administrator\Desktop\navitha\college.txt",'r')
data=file.read()
print(data)
file.close()
import re
file=open(r"C:\Users\Administrator\Desktop\navitha\college.txt",'r+')
sep=re.sub('[ ]','_',data)
print(sep)
