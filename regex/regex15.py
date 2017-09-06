"""
Write a Python program to extract year, month and date from a an url.

"""

import re



url= url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
print(re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url))
print(re.findall(r'/(\d{4})', url))
print(re.findall(r'/(\d{1,2})/(\d{1,2})/', url))

print
url1= "https://www.washingtonpost.com/news/football-insider/wp/201645/019/02/3456789*42/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
print(re.findall(r'/(\d{6})',url1))
print(re.findall(r'/(\d{1,6})',url1))
print(re.findall(r'/(\d{6})/(\d{2})/(\d{2})',url1))
print(re.findall(r'/(\d{6})/(\d{3})/(\d{2})',url1))
print


