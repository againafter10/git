"""

Write a Python program that matches a word at the beginning of a string.

Write a Python program that matches a word at end of string, with optional punctuation.



"""

import re


def word_end(text):
    pattern='\w+\S*$'

    if re.search(pattern,text):
        return "a word at end of string, with optional punctuation " + text
    else:
        return ""

def text_match(text):
    patterns = '^\w'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("The quick brown fox jumps over the lazy dog.   "))
print(text_match(" The quick brown fox jumps over the lazy dog."))


print(word_end("The quick brown fox jumps over the lazy dog."))
print(word_end("The quick brown fox jumps over the lazy dog. "))
print(word_end("The quick brown fox jumps over the lazy dog   "))

