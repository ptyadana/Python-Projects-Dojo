# Coroutine Decorator
# by implmenting decorator and using this decorator allow us to get pre-primed coroutine object
# which we can immediately send values

def coroutine_decorator(func):
    def wrap(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.__next__()
        return cr
    return wrap