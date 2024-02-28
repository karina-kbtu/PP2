import re

pattern = re.compile(r'[ ,.]')
test = open(r"C:\Users\Admin\Desktop\pp2spring\lab5\row.txt","w+")
new_string = re.sub(pattern, ":", test)
print(new_string)