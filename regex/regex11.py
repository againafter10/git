"""
Write a Python program to search some literals strings in a string.
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'

"""
import re

def wordsearch(text,searchfor):
    for i in searchfor:
        if re.search(i,text):
            print "%s is in \" %s \" " %(i,text)
        else:
            print
            print "%s is not in \" %s \" " % (i, text)




searchfor=['fox', 'dog', 'horse']
wordsearch("The quick brown fox jumps over the lazy dog",searchfor)