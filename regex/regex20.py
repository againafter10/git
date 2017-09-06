"""

Write a python program to convert camel case string to snake case string. Go to the editor

Write a python program to convert snake case string to camel case string.

"""
import re

def camel_to_snake(text):
    import re
    str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()


def snake_to_camel(word):
        return ''.join(x.capitalize() or '_' for x in word.split('_'))


string='PythonExercises'
print(camel_to_snake('PythonR45Exercises'))
print(snake_to_camel('python_r45_exercises'))
print
print (string.capitalize())
print (string.lower())