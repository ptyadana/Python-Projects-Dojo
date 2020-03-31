#filter
def only_odd(item):
    return item % 2 != 0

my_list = [1,2,3]
print(my_list)
print(list(filter(only_odd, my_list)))
