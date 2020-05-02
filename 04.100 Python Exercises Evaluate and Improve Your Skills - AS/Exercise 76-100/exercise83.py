# Question: Write a script that detects and prints out your monitor resolution.

# Expected output: 
# Width: 1920,  Height: 1080

# Hint: Use the screeninfo  Python third party library.

# Answer:
from screeninfo import get_monitors

for m in get_monitors():
    print(f'Width: {m.width},  Height: {m.height}')


# Answer2: 
from screeninfo import get_monitors

width=get_monitors()[0].width
height=get_monitors()[0].height

print("Width: %s,  Height: %s" % (width, height))

# Explanation:
# We're using the get_monitors  method of the screeninfo  library which can be installed
#  with pip install screeninfo . The get_monitors  method produces a list 
# like [monitor(1920x1080+0+0), monitor(1280x1024+-1280+-31)]  listing all the monitors 
# connected to the computer. Applying [0]  to that list gives the first monitor object out of the list.
#  Applying width  to that monitor object gives the width of the monitor 
# and the same goes for the height  property.