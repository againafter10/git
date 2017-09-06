"""
Write a Python program to remove multiple spaces in a string.

Write a Python program to remove all whitespaces from a string


Write a Python program to remove everything except alphanumeric characters from a string.


"""

import re
text = "my name    is hawa hawa123iii   "
pattern='[ ]{2,}'
print text
print(re.sub(pattern," " ,text))
pattern='[ ]*'
print(re.sub(pattern,"" ,text))

#to remove everything except alphanumeric characters from a string
text1 = '**//Python Exercises// - 12. '
pattern = re.compile('[\W_]+')
print(pattern.sub('', text1))