import math


def double(x):
    return x * 2


def minus_one(x):
    return x - 1


def squared(x):
    return x * x


# mechnical way
# number = 3
# number = double(number)
# number = minus_one(number)
# number = squared(number)
# print(number)

# -------------
# taste of functional programming way, not a good way yet. just a very basic taste.
# there is no limit to use only the functions we defined, we can also use built in functions too.
# example below math.sqrt
function_list = [
    double,
    minus_one,
    squared,
    math.sqrt
]

number = 3
for func in function_list:
    number = func(number)
print(number)
