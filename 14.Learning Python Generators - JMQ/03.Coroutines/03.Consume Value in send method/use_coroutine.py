# Using Seperate functions and coroutine allow to keep the logic seperate and reusable.
# So, it will be easy to 


from coroutine_decorator_example import coroutine_decorator

# normal function who sends the value and close the coroutine
def sender(filename, target):
    for line in open(filename):
        target.send(line)
    target.close()
    

# check and return the number of matches of search keyword
@coroutine_decorator
def match_counter(string):
    count = 0
    try:
        while True:
            line = yield
            if string in line:
                count += 1
    except GeneratorExit:
        print(f"There are {count} matches of {string}")
        

# check and return the number of instances which length are longer than passed parameter.    
@coroutine_decorator
def longer_than(n):
    count = 0
    try:
        while True:
            line = yield
            if len(line) > n:
                print(line)
                count += 1
    except GeneratorExit:
        print(f"There are {count} names which are longer than {n} characters.")
        
        
        
        
        
        
if __name__ == "__main__":
    c = match_counter("Da")
    sender("data/names.txt", c)
    
    print("")
    
    l = longer_than(14)
    sender("data/names.txt", l)