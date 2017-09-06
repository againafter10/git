"""
Write a Python program to match a string that contains
only upper and lowercase letters, numbers, and underscores.


Write a Python program where a string will start with a specific number


Write a Python program to check for a number at the end of a string

"""

import re
def startnumber(text):
    pattern='^[0-9]+'
    if re.search(pattern,text):
        return "string starts with a specific number " + text
    else:
        return ""


def endnumber(text):
    pattern='[0-9]+$'
    if re.search(pattern,text):
        return "string ends with a specific number " + text
    else:
        return ""



def text_match(text):
    pattern='^[a-zA-Z0-9_]*$'
    if re.search(pattern,text):
        return "only upper and lowercase letters, numbers, and underscores. " + text
    else:
        return ""


print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_Exercises_1"))
print
print(startnumber("23The quick brown fox jumps over the lazy dog."))
print(startnumber("5-2345861"))
print(startnumber("The quick brown fox jumps over the lazy dog."))
print
print(endnumber("23The quick brown fox jumps over the lazy dog."))
print(endnumber("5-2345861"))
print(endnumber("The quick brown fox jumps over the lazy dog."))