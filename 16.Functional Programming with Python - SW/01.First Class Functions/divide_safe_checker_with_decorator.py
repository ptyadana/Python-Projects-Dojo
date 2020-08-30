# This is my version of using decortor for Higher Order functions example.

from functools import wraps


def divide_by_zero_check(func):
    def wrapper(*args):
        if args[1] == 0:
            print("Warning: second argument is Zero.")
            return

        result = func(*args)
        return result
    return wrapper


@divide_by_zero_check
def divide(x, y):
    return x/y


if __name__ == "__main__":
    print(divide(6, 2))
    print(divide(6, 0))
