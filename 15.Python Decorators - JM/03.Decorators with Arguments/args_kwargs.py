'''
Fixed arguments
'''


def print_fib(a, b, c):
    print(a, b, c)


print_fib(1, 1, 2)  # 1 1 2

# give error because the function can only accept only 3 arguments, but 4 were given
# print_fib(1, 1, 2, 3)

'''
Using *args
'''


def print_fib(a, *args):
    print(a)
    print(args)


print_fib(1, 1, 2, 3)  # print 1, (1,2,3)

print_fib(1)  # print 1, ()

'''
Using **kwargs
'''


def print_fib(a, **kwargs):
    print(a)
    print(kwargs)


# print 1, {'se': 1, 'th': 2, 'fo': 3, 'fi': 5}
print_fib(1, se=1, th=2, fo=3, fi=5)

print_fib(1)  # print 1, {}

'''
Using *args and **kwargs
'''


def print_fib(*args, **kwargs):
    print(args)
    print(kwargs)


print("------------")
print_fib(1, 1, 2, 3)  # (1, 1, 2, 3), {}

print_fib(fi=1, se=1, th=2, fo=3)  # (), {'fi': 1, 'se': 1, 'th': 2, 'fo': 3}

print_fib(1, 1, 2, fo=3, fi=5)  # (1, 1, 2), {'fo': 3, 'fi': 5}

print_fib()  # (), {}
