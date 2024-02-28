import re

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

snake_case = open(r"C:\Users\Admin\Desktop\pp2spring\lab5\row.txt","w+")
camel_case_string = snake_to_camel(snake_case)
print(camel_case_string)