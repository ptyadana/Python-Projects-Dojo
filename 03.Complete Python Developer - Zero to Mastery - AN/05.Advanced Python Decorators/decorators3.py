#Decorator Pattern
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("**********")
        func(*args, **kwargs)
        print("**********")
    return wrap_func

@my_decorator
def hello(greeting,emoji, withLove="your love"):
    print(greeting,emoji, withLove)

hello('yo yo', '<3')