my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# difference
my_set.difference(your_set)

# discard
my_set.discard(1)
print(my_set)

# difference_update
my_new_set = {1,2,3,4,5}
my_new_set.difference_update(your_set)
print(my_new_set)

# intersection
# print(my_set.intersection(your_set))
print(my_set & your_set)

# isdisjoint
print(my_set.isdisjoint(your_set))

# issubset
my_set = {4,5}
print(my_set.issubset(your_set))


# issuperset
print(your_set.issuperset(my_set))

# union
# print(my_set.union(your_set))
print(my_set | your_set)
