# Question: Access the third value of key b  from the dictionary.

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

# Expected output: 
# 13  

# Answer
print(d['b'][2])
