""""
Write a Python program that matches a string that has an a followed by zero or more b's

Write a Python program that matches a string that has an a followed by one or more b's.

Write a Python program that matches a string that has an a followed by three b''

Write a Python program that matches a string that has an a followed by two to three 'b'.

"""
import re

def afollowedby2to3b(text):
    pattern='ab{2,3}'
    if re.search(pattern,text):
        return "afollowedby2to3b " + text
    else:
        return text


def afollowedby3b(text):
    pattern = 'ab{3}'
    if re.search(pattern,text):
        return "Found  a followed by three b's " + text
    else:
        return " "
    

def onormoreb(text):
    pattern = 'ab+'
    if re.search(pattern,text):
        return "Found one or more b"
    else:
        return "no one or more b"


def text_match(text):
    patterns = 'ab*'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("ac"))
print(text_match("abc"))
print(text_match("abbc"))
print(text_match("nc"))

print(onormoreb("ac"))
print(onormoreb("abc"))
print(onormoreb("abbb"))
print(onormoreb("bac"))
print(onormoreb("aabbc"))


print (afollowedby3b("abc"))
print (afollowedby3b("abbbbc"))
print (afollowedby3b("abbbc"))
print (afollowedby3b("abc"))



print (afollowedby2to3b("abc"))
print (afollowedby2to3b("abbbbc"))
print (afollowedby2to3b("abbbc"))
print (afollowedby2to3b("abc"))


