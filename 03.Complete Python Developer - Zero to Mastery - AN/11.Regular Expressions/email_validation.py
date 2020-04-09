import re

string = 'test@test25.com'

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

result = pattern.match(string)

print(result.group())


result = pattern.search(string)

print(result)