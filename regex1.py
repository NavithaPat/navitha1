import re
#data=re.findall('[0-9]','abcdf12gh45')
data=re.findall('[0-9]{1,3}','abcd123f12g12345h45')
print(data)