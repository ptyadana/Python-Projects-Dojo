# Question: The code is supposed to get some input from the user, but instead it produces an error. 
# Please try to understand the error and then fix it.

# pass = input("Please enter your password: ") 

# Note: Please use raw_input  instead of input if you are on Python 2. For Python 3 input  is fine.

# Answer:
user_pass = input("Please enter your password: ")
print(user_pass)

# Explanation:
# There was a SyntaxError  error because the syntax to name the variable was wrong since pass  is a reserved keyword in Python. However you can solve that by adding a number to the name or simply choosing another name for the variable.