names_list = ["John", "Suzzie", "Kala", "Liz", "Rob", "Debby"]

reverse_uppercase_names = (name.upper()[::-1] for name in names_list)
print(list(reverse_uppercase_names))

# Or can even break into two parts
# generator can support this
upper_case = (name.upper() for name in names_list)
reverse_uppercase_names = (name[::-1] for name in upper_case)
print(list(reverse_uppercase_names))