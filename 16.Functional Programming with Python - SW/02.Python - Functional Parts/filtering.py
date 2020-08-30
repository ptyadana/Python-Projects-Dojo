number_list = range(10)

# 1) Imperative Way
# we can also use list comprehension if we want here.
even_numbers = []
for item in number_list:
    if item % 2 == 0:
        even_numbers.append(item)

print(even_numbers)


# 2) Functional Way
def is_even(x):
    return x % 2 == 0


even_numbers_using_functional = list(filter(is_even, number_list))
print(even_numbers_using_functional)
