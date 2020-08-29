# very basic decorator
def my_decorator(func):
    def wrapper():
        return "F-I-B-O-N-A-C-C-I"
    return wrapper


def pfib():
    return "Fibonacci"


@my_decorator
def pfib2():
    return "Fibonacci2"


if __name__ == "__main__":

    # before decorator
    print(pfib())

    # After decorator
    pfib = my_decorator(pfib())
    print(pfib)  # we can see in the output that wrapper function got return
    print(pfib())

    # After decorator
    # using @ is same as assigment
    print(pfib2)
    print(pfib2())
