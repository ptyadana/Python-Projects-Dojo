from functools import update_wrapper


class Count:
    def __init__(self, func):
        # update_wrapper is for returning correct doc string and name of the original function
        update_wrapper(self, func)
        self.count = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Current count: {self.count}")
        result = self.func(*args, **kwargs)
        return result


@Count
def fib(n):
    '''return nth number of Fibonacci sequence'''
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print(fib(5))

    # Note: as we can see that there a lot of recursive call to make to get the number.
    # there is a way to optimize this and that's called Memoization
    # Python has built in decorator LRU cache for this.
