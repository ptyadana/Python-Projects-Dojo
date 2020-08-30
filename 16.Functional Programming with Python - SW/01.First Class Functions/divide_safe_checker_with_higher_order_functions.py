def divide(x, y):
    return x/y


def divide_by_zero_check(func):
    def safe_version(*args):
        if args[1] == 0:
            print("Warning: second argument is Zero.")
            return
        return func(*args)
    return safe_version


divide_safe = divide_by_zero_check(divide)
print(divide_safe(10, 5))
print(divide_safe(100, 0))
