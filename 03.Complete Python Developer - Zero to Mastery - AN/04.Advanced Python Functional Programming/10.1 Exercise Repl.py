from functools import reduce

my_list = [5,4,3]

#square
print(my_list)
print(list(map(lambda item: item**2,my_list)))

#list sort by 2nd item
a = [(0,2), (4,3), (9,9), (10,-1)]

print(a)
a.sort(key=lambda item: item[1])
print(a)