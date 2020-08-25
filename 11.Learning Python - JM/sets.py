# https://medium.com/better-programming/a-visual-guide-to-set-comparisons-in-python-6ab7edb9ec41
setA = {1,2,3,4,5}
print("SetA: ", setA)


# list to set
my_list = [10, 20, 30, 40, 50, 1, 2, 3]
setB = set(my_list)
print("SetB: ", setB)

setC = {1,2,3}

# Set-Comparison Methods
# Union
union_result = setA.union(setB)
print("After Union: ", union_result)

# Intersection
intersection_result = setA.intersection(setB)
print("After Intersection: ", intersection_result)

# Difference
differnce_result = setA.difference(setB)
print("After difference SetA - SetB: ", differnce_result)
print("After difference SetA - SetB: ", setB.difference(setA))

# Symmetric Difference
sym_difference_result = setA.symmetric_difference(setB)
print("After Symmetic Difference SetA - SetB : ", sym_difference_result)
print("After Symmetic Difference SetB - SetA : ", setB.symmetric_difference(setA))

# subset
print("Is setC subset of setA : ", setC.issubset(setA))

# superset
print("Is setA superset of setC: ", setA.issuperset(setC))

# disjoint
print("Is SetC and SetB disjoint? ", setC.isdisjoint(setB))