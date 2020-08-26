# Coroutine Decorator
# by implmenting decorator and using this decorator allow us to get pre-primed coroutine object
# which we can immediately send values

def coroutine_decorator(func):
    def wrap(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.__next__()
        return cr
    return wrap

@coroutine_decorator
def coroutine_example():
    while True:
        x = yield
        # do something
        print(x)
        
        
        

if __name__ == "__main__":
    c = coroutine_example()
    c.send("hello")