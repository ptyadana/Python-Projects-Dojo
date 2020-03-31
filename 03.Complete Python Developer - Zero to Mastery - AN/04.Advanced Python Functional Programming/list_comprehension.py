my_list = [char for char in 'hello']
print(my_list)

#0 - 99
my_list2 = [num for num in range(0,100)]
print(my_list2)

#square of 0-99
my_list3 = [num**2 for num in range(0,100)]
print(my_list3)

#only even number of (square of 0-99)
my_list4 = [num**2 for num in range(0,100) if num%2 == 0]
print(my_list4)