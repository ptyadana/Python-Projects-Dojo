from time import perf_counter
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start

        args = str(*args)
        print(f"{func.__name__}({args}) = {result} => Duration: {duration:.8f}seconds")

        return result
    return wrapper


@timer
def fib(n):
    '''return nth value from Fibonacci sequence '''
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print(fib(20))
