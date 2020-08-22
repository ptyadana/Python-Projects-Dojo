numbers = [1, 2, 3, 4, 5]
doubled = [num*2 for num in numbers]
print(doubled)


name = "harry potter"
all_cap = [letter.upper() for letter in name]
print(all_cap)


results = [bool(val) for val in [0, [], ""]]
print(results)