from functools import wraps


def bold(func):
    '''Bold decorator'''
    @wraps(func)
    def wrapper():
        result = "<b>" + func() + "</b>"
        return result
    return wrapper


def italics(func):
    '''italic decorator'''
    @wraps(func)
    def wrapper():
        result = "<i>" + func() + "</i>"
        return result
    return wrapper


@bold
@italics
def printfib():
    '''return Fibonacci'''
    return 'Fibonacci'


if __name__ == "__main__":
    print(printfib())
