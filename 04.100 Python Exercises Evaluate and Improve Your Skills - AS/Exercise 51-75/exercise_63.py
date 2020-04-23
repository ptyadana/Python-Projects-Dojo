# Question: Create a program that once executed the programs prints Hello  instantly first,
#  then it prints it after 1 second, then after 2, 3, 
# and then the program prints out the message "End of the Loop" and stops.

# Expected output: 

# Hello
# Hello
# Hello
# Hello
# End of Loop

import time

second = 0
while True:
    print('Hello')
    second += 1

    if second > 3:
        print('End of the loop')
        break

    time.sleep(second)
    
