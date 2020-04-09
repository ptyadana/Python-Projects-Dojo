import re

string = 'search inside of this text please!'

a = re.search('this',string)

#span => show start and end indexes
print(a.span())

#start => start index
print(a.start())
print(a.end())

print(a.group())