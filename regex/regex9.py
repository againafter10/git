"""
Write a Python program to remove leading zeros from an IP address

input = "216.08.094.196"
output = "216.8.94.196"

"""
import re
ip = "216.08.094.196"
string = re.sub('\.[0]*', '.', ip)
#re.sub(pattern,replacewith,stringwheretodothis)
print string

new= " abc next tttt nhe"
print(re.sub('c n','###',new))