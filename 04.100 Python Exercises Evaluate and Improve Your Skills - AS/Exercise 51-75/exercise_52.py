# Question: The code is supposed to ask the user to enter their name and surname and 
# then it prints out those user submitted values. Instead, the code throws a TypeError. 
# Please fix it so that the expected output is printed out.

# firstname = input("Enter first name: ")
# secondname = input("Enter second name: ")
# print("Your first name is %s and your second name is %s" % firstname, secondname)
# Expected output: 

# Your first name is John and your second name is Smith 

# Answer:
firstname = input("Enter first name: ")
secondname = input("Enter second name: ")
print("Your first name is %s and your second name is %s" % (firstname, secondname))
print(f'Your first name is {firstname} and your second name is {secondname}')

# Explanation:
# Each of the %s  placeholders expects one value after %  to be replaced with, but you need to pass these values inside a tuple. So, putting variables firstname  and secondname  inside a tuple fixes the code.