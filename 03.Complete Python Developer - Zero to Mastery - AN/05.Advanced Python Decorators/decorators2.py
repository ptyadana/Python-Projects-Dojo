#Decorators are boosters which supercharge the function
#Decorator 
# - needs to accept the function as parameter
# - wrarp it around in wrapper function
# - returned the boosted wrapped function

def my_decorator(func):
    def wrap_func():
        print("**********")
        func()
        print("**********")
    return wrap_func


def hello():
    print("Hellllooooo")

hello()

print("--------------")

@my_decorator
def new_hello():
    print("New Hellllooooo")

new_hello()

@my_decorator
def bye():
    print("Byeeeeeeeeeeee")

bye()