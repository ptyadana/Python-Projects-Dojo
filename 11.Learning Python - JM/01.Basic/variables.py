# 
# Example file for variables
#

# Declare a variable and initialize it
x = 100
print(x)

# # re-declaring the variable works
x = "abc"
print(x)

# # ERROR: variables of different types cannot be combined
# print("hello" + 123)
print("hello" + str(123))

# Global vs. local variables in functions
def some_func():
    # global x
    x = 999
    print(x)


some_func()
print(x)
