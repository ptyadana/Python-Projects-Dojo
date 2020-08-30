def add(x, y, z):
    return x + y + z

# Using Partial


def add_partial(x):
    def add_others(y, z):
        return x + y + z
    return add_others


add_5 = add_partial(5)
print(add_5(6, 7))


# 2) we can always change the way we pass for partial
def add_partial_2(x, y):
    def add_others(z):
        return x + y + z
    return add_others


add_5_and_7 = add_partial_2(5, 7)
print(add_5_and_7(6))
