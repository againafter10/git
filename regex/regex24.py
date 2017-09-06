"""
Write a Python program to print all words having S
"""
def casespecific(text):
    for i in text.split():
        if 'S' in i:
            print i


def nocase(text):
    #test=text.lower()
    for i in text.lower().split():
        if 's' in i:
            print i,


test = "I have a word that has no S in it."
casespecific(test)
nocase(test)