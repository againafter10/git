"""
Write a Python program that matches a word containing 'z'.

Write a Python program that matches a word containing 'z', not start or end of the word.
"""

import re

def wordwithz(text):
    pattern = 'z*'
    if re.search(pattern,text):
        return "matches a word containing 'z' " + text
    else:
        return ""


def zinbetween(text):
    patterns = '\Bz\B'
    if re.search(patterns, text):
        return "matches a word containing 'z' in between " + text
    else:
        return ""





print(wordwithz("The quick brown fox jumps over the lazy dog"))
print(wordwithz("The quick brozzzzn fox jumps over the lazy dog"))
print(wordwithz("The quick browzzzzzzzn fox jumps over the lazy dog"))
print

print(zinbetween("zThe quick brown fox jumps over the lazy dog"))
print(zinbetween("The quick brozzzzn fox jumps over the lazy dog"))
print(zinbetween("The quick browzzzzzzzn fox jumps over the lazy dog"))