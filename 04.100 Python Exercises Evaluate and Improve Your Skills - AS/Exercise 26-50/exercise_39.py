# Question: The script is supposed to output the cosine of angle 1 radian, but instead it is throwing an error. Please fix the code so that it prints out the expected output.

# import math
# print(math.cosine(1))

# Expected output:
# 0.5403023058681397   


# Answer:
import math
print(math.cos(1))
print(dir(math))

# Hint: You could get a list of all available methods of the math module with dir(math) and see whether cosine is there or not.