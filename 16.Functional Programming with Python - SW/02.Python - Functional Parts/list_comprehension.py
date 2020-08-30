# List Comprehension is sort of like Map + Filter

numbers_list = range(10)

# Basic list comprehension (map)
doubled = [x * 2 for x in numbers_list]
print(doubled)

# Basic list comprehension (filter)
evens = [x for x in numbers_list if x % 2 == 0]
print(evens)

# list comprehension (map + filter)
doubled_evens = [x * 2 for x in numbers_list if x % 2 == 0]
print(doubled_evens)

# list comprehension (if else)
processed_data = [x * 2 if x % 2 == 0 else x * 10 for x in numbers_list]
print(processed_data)
