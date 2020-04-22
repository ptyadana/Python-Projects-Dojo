# Question: Filter the dictionary by removing all items with a value of greater than 1.

d = {"a": 1, "b": 2, "c": 3}

# Expected output: 
# {'a': 1}  

# Answer
my_dict = {key:value for key,value in d.items() if value <=1 }
print(my_dict)

# Explanation: 
# Here we're using a dictionary comprehension. The comprehension is the expression inside dict() . The comprehension iterates through the existing dictionary items and if an item is less or equal to 1,the item is added to a new dict. This new dict is assigned to the existing variable d  so we end up with a filtered dictionary in d.