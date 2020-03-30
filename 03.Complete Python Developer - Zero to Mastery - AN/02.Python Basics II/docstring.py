def hello(name):
    '''Info: accepts parameter and say hello to that name
    name: parameter'''
    print(f"hello {name}")


#how to see docstring of a certain function
#way 1
print(help(hello))

#way 2
print(hello.__doc__)