import re
pan=re.findall('[A-Z]{5} ?[0-9]{4}[A-Z]','ABCDE 1234F')
print(pan)