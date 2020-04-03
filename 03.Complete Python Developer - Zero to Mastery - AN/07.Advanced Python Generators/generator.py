#generator
#yeild pause the function and give the value
#generator doesn't store the value in memory which is different like using a list 
#if we are using a list, list store the values in memory which might take resources and more time to process
def generator_function(num):
    for i in range(num):
        yield i

for item in generator_function(100):
    print(item)
