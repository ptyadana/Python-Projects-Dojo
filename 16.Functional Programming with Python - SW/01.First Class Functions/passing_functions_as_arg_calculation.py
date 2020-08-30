def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


# combined function : pssing function as argument
def combine_2_and_3(func):
    return func(2, 3)


print(combine_2_and_3(add))
print(combine_2_and_3(subtract))

print(combine_2_and_3(min))
print(combine_2_and_3(max))
