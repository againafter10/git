"""

 Write a Python program to find sequences of one upper case letter followed by lower case letters
"""
import re

def text_match(text):
    pattern='^[A-Z]+[a-z]+'
    if re.search(pattern,text):
        return " found sequences of one upper case letter followed by lower case letters  " + text
    else:
        return ""

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))