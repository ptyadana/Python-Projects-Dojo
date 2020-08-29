def fibonacci_three(a, b, c):
    '''Accepts as 3 input fibonacci numbers'''
    def get_three():
        '''returns 3 fibonacci numbers'''
        return a, b, c
    return get_three


if __name__ == "__main__":
    print(fibonacci_three(1, 2, 3))

    f = fibonacci_three(1, 2, 3)
    print(f)
    # as f is assigned with the function returned, it can act as function again and will return those tuples.
    print(f())
