file=open(r"C:\Users\Administrator\Desktop\index.txt",'r')
data=file.read()
print(data)
file.close()
import re
vowel=re.findall('[aeiou]{1}',r'C:\Users\Administrator\Desktop\index.txt')
print(len(vowel))
