#Rule for parameters: params, *args, default parameters, **kwargs
#def hello(name, *args, age=25, **kwargs)

# *args    **kargs (keywords arguments)

def super_func(*args):
    print(args)
    return sum(args)

print(super_func(1,2,3,4,5))
print(super_func(1))


print("-------------------------")
def super_func2(**kwargs):
    print(kwargs)
    total = 0
    for item in kwargs.values():
        total += item
    return total

print(super_func2(num1=5,num2=10))

