# Regular Expressions

import re

string = "Search this string!"
pattern = re.compile('this')

search = re.search('this', string)
print(search.start())
print(search.end())

a = pattern.search(string)
print(a)

b = pattern.match(string)
print(b)

c = pattern.fullmatch(string)
print(c)

d = pattern.findall(string)
print(d)