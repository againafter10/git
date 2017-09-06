"""
Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

"""
import re
def text_match(text):
    pattern='a*b$'
    if re.search(pattern,text):
        return "found an a followed by anything and ending with b " + text
    else:
        return ""

print(text_match("aab_cbbbc"))
print(text_match("ab"))
print(text_match("aab_Abbbcbbbbbb"))
print(text_match("aab_Abbbcbaaaaa"))
print(text_match("aab_Abbbcbaaaaa"))
