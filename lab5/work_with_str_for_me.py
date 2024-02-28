'''
1. Matching 'a' followed by zero or more 'b's:

import re

pattern = re.compile(r'ab*')
test_string = "ab abb abbb"
matches = pattern.finditer(test_string)
for match in matches:
    print(match)


2. Matching 'a' followed by two to three 'b':

import re

pattern = re.compile(r'ab{2,3}')
test_string = "ab abb abbb"
matches = pattern.finditer(test_string)
for match in matches:
    print(match)


3. Finding sequences of lowercase letters joined with an underscore:

import re

pattern = re.compile(r'[a-z]+_[a-z]+')
test_string = "hello_world python_programming"
matches = pattern.finditer(test_string)
for match in matches:
    print(match)


4. Finding sequences of one upper case letter followed by lower case letters:

import re

pattern = re.compile(r'[A-Z][a-z]+')
test_string = "Hello World Python Programming"
matches = pattern.finditer(test_string)
for match in matches:
    print(match)


5. Matching 'a' followed by anything, ending in 'b':

import re

pattern = re.compile(r'a.*b')
test_string = "axxxxxb ayyyyb azzb"
matches = pattern.finditer(test_string)
for match in matches:
    print(match)


6. Replacing all occurrences of space, comma, or dot with a colon:
import re

pattern = re.compile(r'[ ,.]')
test_string = "Hello, world. How are you?"
new_string = re.sub(pattern, ":", test_string)
print(new_string)

7. Converting snake case string to camel case string:

import re

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

snake_case_string = "hello_world_python"
camel_case_string = snake_to_camel(snake_case_string)
print(camel_case_string)

8. Write a Python program to split a string at uppercase letters:

import re

def split_at_uppercase(s):
    return re.findall('[A-Z][^A-Z]*', s)

s = "SplitThisStringAtUpperCaseLetters"
result = split_at_uppercase(s)
print(result)


9. Write a Python program to insert spaces between words starting with capital letters:

import re

def insert_spaces_at_capitals(s):
    return re.sub(r'(\w)([A-Z])', r'\1 \2', s)


s = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
result = insert_spaces_at_capitals(s)
print(result)


10.Write a Python program to convert a given camel case string to snake case:

import re

def camel_to_snake(s):
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)).lower()

s = "ConvertCamelCaseStringToSnakeCase"
result = camel_to_snake(s)
print(result)
'''