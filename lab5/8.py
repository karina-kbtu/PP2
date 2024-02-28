import re

def split_at_uppercase(s):
    return re.findall('[A-Z][^A-Z]*', s)

s = open(r"C:\Users\Admin\Desktop\pp2spring\lab5\row.txt","w+")
result = split_at_uppercase(s)
print(result)