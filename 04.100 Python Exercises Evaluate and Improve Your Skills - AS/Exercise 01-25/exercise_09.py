# Question: Complete the script so that it prints out a list slice containing the last three items of list letters .

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# Expected output:
# ['h', 'i', 'j'] 

# Answer:
print(letters[-3:])

# Explanation: 
# [-3:]  means from item with index -3  (i.e. h ) to the very last item of the list. When you don't put any index to the right of the colon everything is included and upper-bound exclusivity is ignored.