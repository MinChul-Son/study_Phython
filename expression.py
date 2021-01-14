import re

p= re.compile('[a-z]+')
m = p.match('python')
print(m)
m = p.search('python')

m= p.findall('life is too short')
print(m)