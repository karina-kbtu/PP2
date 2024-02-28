import re

def insert_spaces_at_capitals(s):
    return re.sub(r'(\w)([A-Z])', r'\1 \2', s)

s = open(r"C:\Users\Admin\Desktop\pp2spring\lab5\row.txt","w+") 
result = insert_spaces_at_capitals(s)
print(result)