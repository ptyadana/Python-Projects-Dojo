# Question: Create a program that once executed the program prints Hello  instantly first, 
# then it prints it after 1 second, then after 2, 3, 4, and so on the interval increases between prints.

# Expected output: 

# ...
# Hello
# Hello
# Hello
# Hello
# Hello
# Hello
# ...

# Answer:
import time

second = 0
while True:
    print('Hello')
    second += 1
    time.sleep(second)
    