# Question: Complete the script so that it prints out a list slice containing letters a, c, e, g, and i. 

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# Expected output: 
# ['a', 'c', 'e', 'g', 'i'] 


# Answer:
print(letters[::2])


# Explanation: 
# The complete syntax of list slicing is [start:end:step] . When you don't pass a step, Python assumes the step is 1. [:]  itself means get everything from start to end. So, [::2]  means get everything from start to end at a step of two.