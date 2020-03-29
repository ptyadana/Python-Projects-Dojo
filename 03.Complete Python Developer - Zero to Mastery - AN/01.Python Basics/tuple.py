# tuple are immutables
my_tuple = (1,2,3,4,5,5,5)

for item in my_tuple:
    print(item)

print(2 in my_tuple)
print(my_tuple[2])

print(my_tuple)

x,y,*other = my_tuple
sliced_tuple = my_tuple[2:]
print(x)
print(y)
print(other)
print(sliced_tuple)

#count
print(my_tuple.count(5))

#index
print(my_tuple.index(5))

#len
print(len(my_tuple))