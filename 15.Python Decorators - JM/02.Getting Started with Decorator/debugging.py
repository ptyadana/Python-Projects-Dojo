from functools import wraps


def make_posh(func):
    '''This is the function decorator'''
    def wrapper():
        '''This is the wrapper function'''
        print("+---------+")
        print("|         |")
        result = func()
        print(result)
        print("|         |")
        print("+=========+")
        return result
    return wrapper


def make_posh3(func):
    '''This is the function decorator'''

    @wraps(func)
    def wrapper():
        '''This is the wrapper function'''
        print("+---------+")
        print("|         |")
        result = func()
        print(result)
        print("|         |")
        print("+=========+")
        return result

    # the following 2 lines are same as decorating @wraps
    # wrapper.__doc__ = func.__doc__
    # wrapper.__name__ = func.__name__

    return wrapper


def printfib():
    '''Print out Fibonacci'''
    return ' Fibonacci '


@make_posh
def printfib2():
    '''Print out Fibonacci2'''
    return ' Fibonacci2 '


@make_posh3
def printfib3():
    '''Print out Fibonacci3'''
    return ' Fibonacci3 '


if __name__ == "__main__":
    # when we try to debug printfib, we can get original name info
    print(printfib.__name__)
    print(printfib.__doc__)

    # if we use decorator for printfib2, we lose the original information and instead get wrapper info
    print("--------------")
    print(printfib2.__name__)
    print(printfib2.__doc__)

    # we can fix this issue by assigning those meta data information insides the decorator function
    # or the cleaner way is using wraps decorator which give the same results
    print("---------------")
    print(printfib3.__name__)
    print(printfib3.__doc__)
