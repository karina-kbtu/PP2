import re

pattern = re.compile(r'[a-z]+_[a-z]+')
test = open(r"C:\Users\Admin\Desktop\pp2spring\lab5\row.txt","w+")
matches = pattern.finditer(test)
for match in matches:
    print(match)