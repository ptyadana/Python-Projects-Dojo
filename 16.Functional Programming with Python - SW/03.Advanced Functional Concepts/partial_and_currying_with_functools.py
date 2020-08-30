from functools import partial


def add(x, y, z):
    return x + y + z


add_5 = partial(add, 5)
print(add_5(6, 7))
