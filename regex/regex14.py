"""
Write a Python program to replace whitespaces with an underscore and vice versa.

"""
import re

text = 'Python exercises,     PHP exercises, C# exercises'
pattern = ' '
text2 = re.sub(pattern,'_',text)
print text2