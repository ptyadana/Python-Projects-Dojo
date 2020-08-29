from functools import wraps


def munch(start, end):
    def do_munch(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_string = ""
            result = func(*args, **kwargs)

            for index, char in enumerate(result):
                c = 'x' if start <= index < end else char
                new_string += c
            return new_string
        return wrapper
    return do_munch


@munch(1, 5)
def fib():
    return 'Fibonacci'


if __name__ == "__main__":
    print(fib())
