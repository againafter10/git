"""
Write a Python program to abbreviate 'Street' as 'St' in a given string.

Write a Python program to abbreviate  end 'Street' as 'St' in a given string.

"""
import re
street = 'unit 2 Barton Street Street'
pattern = 'Street'
replace='St'
print (re.sub(pattern,replace,street))

pattern = 'Street$'
print (re.sub(pattern,replace,street))