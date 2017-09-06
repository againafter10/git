"""
Write a Python program to search a literals string in a string
and also find the location within the original string where the pattern occurs

Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'

"""

import re
pattern = ['fox','horse','tiger','brown']
text = 'The quick brown fox jumps over the lazy dog.'
for i in pattern:
    if re.search(i,text):
        match = re.search(i, text)
        s = match.start()
        e = match.end()
        print('Found "%s" in "%s" from %d to %d ' % (i,text, s, e))