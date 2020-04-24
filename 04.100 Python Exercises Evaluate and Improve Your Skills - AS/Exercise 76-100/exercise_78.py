#create a program that generate a password of 6 random alphanumeric characters in the range
#abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?

# Answer 1:
import random

st = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
password = ''
for i in range(6):
    password += random.choice(st)
print(password)


# Answer 2: 

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
chosen = random.sample(characters, 6)
password = "".join(chosen)
print(password)

# Explanation:
# We're importing the random  module and using its sample  method which picks 6 random items from the characters  sequence. The items are stored in list chosen . Then we use a string join  method to join the list items to a string.

