numbers_list = range(10)

# simple lambda
# add = lambda x, y : x+y
# print(add)

doubled_numbers = list(map(lambda x: x*2, numbers_list))
print(doubled_numbers)


# using lambda for multiplier
def multiplier(multipler_num):
    return lambda x: x * multipler_num


doubled = multiplier(2)
print(doubled(4))
