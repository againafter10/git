"""

Write a Python program to extract values between quotation marks of a string

"""

import re

text = '"Python", "PHP", "Java"'
pattern='"(.*?)"'


print(re.findall(pattern,text))