import re
vehicle=re.findall('AP ?[0-3][1-9] ?[A-Za-z] ?[0-9]{4}','AP 01 A 1234')
print(vehicle)