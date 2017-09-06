"""
Write a Python program to search the numbers (0-9) of length between 4 to 7 in a given string

"""
import re
def text_match(text):
    pattern='[0-9]{4,7}'
    if re.search(pattern,text):
        print(re.findall(pattern,text))
        print
        return "numbers (0-9) of length between 1 to 3 in " + text
    else:
        return ""

print (text_match("Exercises number 1, 12, 13, and 345 are important"))
print (text_match("Exercises number 1111, 12333 are easy"))


