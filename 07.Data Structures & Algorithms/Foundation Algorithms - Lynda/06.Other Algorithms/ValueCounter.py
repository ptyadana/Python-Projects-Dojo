# using a hashtable to count individual items


# define a set of items that we want to count
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# create a hashtable object to hold the items and counts
fruits_counter = {}

# iterate over each item and increment the count for each one
for item in items:
    if item in fruits_counter.keys():
        fruits_counter[item] = fruits_counter[item] + 1
    else:
        # set default count = 0
        fruits_counter.setdefault(item, 0)

# print the results
print(fruits_counter)
