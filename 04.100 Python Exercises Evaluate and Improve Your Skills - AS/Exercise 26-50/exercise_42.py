# Question: Print out in each line the sum of homologous items of the two sequences.

a = [1, 2, 3]
b = (4, 5, 6)

# Expected output: 

# 5
# 7
# 9

# Answer 1:
for index,item in enumerate(a):
    print(a[index]+b[index])

# Answer 2:
print(zip(a,b))