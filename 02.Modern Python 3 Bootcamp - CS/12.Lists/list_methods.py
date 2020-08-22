
""" append and extend"""

first_line = [1,2,3,4,5]

first_line.append(6)
print(first_line)

# first_line.append(7,8,9) #doesn't work

first_line.append([7,8,9])
print(first_line)

correct_list = [1,2,3,4,5]
correct_list.extend([6,7,8,9,10])
print(correct_list)

""" insert """
print()
correct_list.insert(0, 100)
print(correct_list)


""" remove """
print()
first_line.remove(5)
print(first_line)


""" clear """
print()
first_line.clear()
print(first_line)

""" pop """
print()

print(correct_list)

correct_list.pop()
print(correct_list)

correct_list.pop(2)
print(correct_list)


""" index """
print()

lst = ["A", "B", "C", "D", "E", "B", "F"]
print(lst)
print(lst.index("E"))

print(lst.index("B"))
print(lst.index("B", 3, 7))


""" count """
print()

print(lst.count("A"))
print(lst.count("B"))


""" reverse """
print()

correct_list = [1,2,3,4,5]
print(correct_list)

correct_list.reverse()
print(correct_list)


""" sort """
print()

another_list = [23, 11, 456, 2, 1, 52]
print(another_list)

another_list.sort()
print(another_list)


""" join """
lst = ["Coding", "is", "fun"]
st = " ".join(lst)
print(st)


""" slicing """
lst = ["A", "B", "C", "D", "E"]
print(lst)
print(lst[1::2])
print(lst[::2])
print(lst[-2:])
print(lst[::-1])
print(lst[1::-1])


""" swapping values """
names = ["Harry", "Potter"]
names[0], names[1] = names[1], names[0]
print(names)