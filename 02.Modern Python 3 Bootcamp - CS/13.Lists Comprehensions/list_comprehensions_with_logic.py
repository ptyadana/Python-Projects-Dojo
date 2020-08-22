numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = [num for num in numbers if num%2 == 0]
print(even)

# even odd checker
results = [f"{num} - even" if num%2 == 0 else f"{num} - odd" for num in numbers]
print(results)

# vowel filter (no vowel)
my_string = "This is so much fun !"
results = "".join(char for char in my_string if char not in "aeiou")
print(results)