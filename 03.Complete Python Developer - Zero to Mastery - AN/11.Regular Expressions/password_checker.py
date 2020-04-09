# at least 8 chars long
# contains any sort of letters, numbers, $%#@
# has to end with number

import re

string = "ABdasdf3$@%0"

pattern = re.compile(r"([A-Za-z0-9$%#@]{7,}[0-9])")

result = pattern.fullmatch(string)

print(result)