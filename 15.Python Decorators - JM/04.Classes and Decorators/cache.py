from time import perf_counter
from functools import wraps
from functools import lru_cache


def timer(func):
    total = 0  # scope: timer()

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal total
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        total += duration  # scope : wrapper()
        arg = str(*args)
        print(f'{func.__name__}({arg}) = {result} -> {duration:.8f}')
        print(f'Total duration: {total:.8f}')
        return result
    return wrapper


@lru_cache(maxsize=None)
@timer
def fib(n):
    '''Return the nth value from the Fiboanacci sequence'''
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    fib(5)
