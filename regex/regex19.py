"""
Write a Python program to find all five characters long word in a string.


Write a Python program to find all three, four, five characters long words in a string


Write a Python program to find all words which are at least 2 characters long in a string.

"""
import re
text = 'The quick brown fox jumps over:the lazy dog.'
print(re.findall(r"\b\w{5}\b", text))

print(re.findall(r"\w{5}", text)) #assumes only alphabets to be in the word
print(re.findall(r"\S", text)) # all characters without space

# to find all three, four, five characters long words in a string
text = 'The quick brown fox jumps over:the lazy dog.'
print(re.findall(r'\w{3,4}\w',text))


#to find all words which are at least 2 characters long in a string.
print(re.findall(r'\w{2,}',text))