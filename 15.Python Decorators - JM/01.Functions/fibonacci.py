def fibonacci(n):
    '''Return nth number of fibonacci sequence'''
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    for i in range(1, 10):
        print(fibonacci(i))
