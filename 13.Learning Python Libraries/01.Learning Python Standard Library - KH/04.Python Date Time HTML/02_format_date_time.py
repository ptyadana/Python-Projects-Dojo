# Getting more control over formatting
from datetime import datetime

now = datetime.now()

print(now.strftime("%a %A %d"))

print(now.strftime("%b %B %m"))

print(now.strftime("%a %B %d"))
print(now.strftime("%A %B %d"))

print(now.strftime("%H:%M:%S %p"))

print(now.strftime("%y %Y"))