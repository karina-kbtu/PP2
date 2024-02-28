import re

def camel_to_snake(s):
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)).lower()

s = open(r"C:\Users\Admin\Desktop\pp2spring\lab5\row.txt","w+")
result = camel_to_snake(s)
print(result)