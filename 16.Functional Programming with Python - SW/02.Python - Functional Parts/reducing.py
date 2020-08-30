from functools import reduce

numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# acc is accumulator which is current value, x is current element


def get_sum(acc, x):
    print(f"Accumulator is {acc}, x is {x}")
    return acc + x


# Reduce squashed down the input elements into single value output
sum = reduce(get_sum, numbers_list)
print(sum)

# We can also pass initial value as 3rd argument
total = reduce(get_sum, numbers_list, 1000)
print(total)
