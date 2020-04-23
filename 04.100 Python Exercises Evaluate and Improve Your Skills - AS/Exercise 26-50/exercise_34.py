# Question: The following script throws a NameError  in the last line saying that c  is not defined. Please fix the function so that there is no error and the last line is able to print out the value of c  (i.e. 1 ).

# def foo(): 
#     c = 1 
#     return c 

# foo() 
# print(c)

# Expected output:
# 1 

# Answer:

def foo(): 
    global c
    c = 1 
    return c 

foo() 
print(c)


# Explanation:
# Adding global c  fixes the code. That line makes available name c  in the global namespace. Therefore,  print is able to access variable c .
