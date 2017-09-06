"""
Write a Python program to find the occurrence and position of the substrings within a string

"""
import re

text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

if re.search(pattern,text):
    match=re.search(pattern,text)
    s=match.start()
    print ( "%s start at position %s"  %(pattern,s))