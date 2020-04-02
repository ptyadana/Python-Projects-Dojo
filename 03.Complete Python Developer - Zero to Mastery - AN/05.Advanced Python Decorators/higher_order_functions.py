#HOC (Highter Order Functions)
#HOC has 2 types
#1) Functions that accept function as parameter
#2) Functions that return function

#1) Functions that accept function as parameter
def greet(func):
    func()

#2) Functions that return function
def greet2():
    def new_func():
        print("hello")
    return new_func


print(greet2()())