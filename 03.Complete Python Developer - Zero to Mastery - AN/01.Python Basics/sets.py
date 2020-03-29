#set is the unordered collection of UNIQUE objects
my_set = {1,2,3,4,5,5,5,5,5}

print(my_set)

my_set.add(100)
print(my_set)

my_set.add(50)
print(my_set)

my_list = [1,2,3,4,5,5,5,5,5]
unique_set = set(my_list)
print(unique_set)


my_set.add(200)
print(my_set)
my_set.remove(100)
print(my_set)
