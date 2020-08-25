collection = ["gold", "silver", "bronze"]

# list comprehension
new_list = [item.upper for item in collection]

# generator expression
# it is similar to list comprehension, but use () round brackets
my_gen = (item.upper for item in collection)