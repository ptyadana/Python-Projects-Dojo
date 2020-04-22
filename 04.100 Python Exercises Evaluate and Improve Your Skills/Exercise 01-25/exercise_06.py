# Question: Please complete the script so that it prints out a list slice containing items d , e , and f .

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output: 
# ['d', 'e', 'f'] 


# Answer:
print(letters[3:6])

# Explanation: 
# d  has an index of 3  here, e  has an index of 4 , and f  has an index of 5, but since the slicing syntax is upper-bound exclusive, we need to pass 6  as the upper bound.