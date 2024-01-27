import re
email=re.findall('[a-zA-Z0-9]+\.?[a-zA-Z0-9]*\@gmail\.com','abcd123.xyz@gmail.com')
print((email))