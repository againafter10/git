"""
Write a Python program to remove multiple spaces in a string.

Write a Python program to remove all whitespaces from a string


Write a Python program to remove everything except alphanumeric characters from a string.


"""

import re

def searchlist(text):
    pattern='a'
    return (re.search(pattern,text))

def findlist(text):
    pattern='a'
    return (re.findall(pattern,text))


string=searchlist("my name    is hawa hawa123iii   ")
print (string)
print(string.start())
print(string.end())

string=findlist("my name    is hawa hawa123iii   ")
print string
