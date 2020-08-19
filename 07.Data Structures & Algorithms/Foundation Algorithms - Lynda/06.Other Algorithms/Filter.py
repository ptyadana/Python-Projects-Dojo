# use a hashtable to filter out duplicate items


# define a set of items that we want to reduce duplicates
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# create a hashtable to perform a filter
fruits = {}

# loop over each item and add to the hashtable
for item in items:
    fruits[item] = 0

# create a set from the resulting keys in the hashtable
result = set(fruits.keys())
print(result)