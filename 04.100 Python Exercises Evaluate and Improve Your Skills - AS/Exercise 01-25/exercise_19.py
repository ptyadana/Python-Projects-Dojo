# Question: Add a new pair of key (e.g. c ) and value (e.g. 3 ) to the dictionary and print out the new dictionary.

d = {"a": 1, "b": 2}

# Expected output: 
# {'a': 1, 'c': 3, 'b': 2} 

#Answer
d['c']=3
print(d)

# Explanation: 
# Adding pairs of keys and values is straightforward as you can see. Note though that you cannot fix the order of the dictionary items. Dictionaries are unordered collections of items.