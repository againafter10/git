"""
Write a Python program to find sequences of lowercase letters joined with a underscore.
"""
import re
def text_match(text):
    #pattern='^[a-z]+_[a-z]+$'
    pattern = '^[a-z]+_[a-z]+$'
    if re.search(pattern,text):
        return "find sequences of lowercase letters joined with a underscore   " + text
    else:
        return " "

print (text_match("aab_cbbbc"))
print (text_match("aab_BBBbc"))
print (text_match("aAb_cbbbc"))
