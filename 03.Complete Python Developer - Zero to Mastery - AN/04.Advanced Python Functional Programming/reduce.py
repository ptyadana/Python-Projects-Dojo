#reduce
from functools import reduce

my_list = [1,2,3]
your_list = (100,200,300)
their_list = (1000,2000,3000)

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 0))
