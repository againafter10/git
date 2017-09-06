"""

Write a Python program to replace all occurrences of space, comma, or dot with a colon.

Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon

"""

import re
def replacemax2(text):
    pattern='[ ,.]'
    rep=':'
    return (re.sub(pattern,rep,text,2))


def replace(text):
    pattern='[ ,.]'
    rep=':'
    return (re.sub(pattern,rep,text))


print(replace('Python Exercises, PHP exercises.'))
print(replacemax2('Python Exercises, PHP exercises.'))
