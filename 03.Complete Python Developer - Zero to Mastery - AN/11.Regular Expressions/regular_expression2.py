import re

string = 'search inside of this text please!'

pattern = re.compile(r"([a-zA-z]).([a])")

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print(a)
print(b)
print(c)
print(d)

print("---------------")
print(a.group())

