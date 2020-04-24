# Question: Create a script that asks the user to enter their age and the script calculates 
# the user's year of birth and prints it out in a string like in the expected output. 
# Please make sure you generate the current year dynamically.

# Expected output: 
# We think you were born back in 1988

# Answer:
from datetime import datetime

try:
    user_input = int(input('Please enter your age: '))
    dob_year = datetime.now().year - user_input

    print(f'We think you were born back in {dob_year}')
except:
    print('Invalid input. Please try again.')

# Explanation:
# We're getting user input and we are converting it to an integer since input  loads everything as a string. Then we produce the current year dynamically with datetime.now().year  and we subtract the age from that to find out the year of birth. Lastly, in line 5, we use string formatting to produce a string with the year inside it.


