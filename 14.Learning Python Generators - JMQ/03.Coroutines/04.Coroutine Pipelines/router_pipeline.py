from coroutine_decorator_example import coroutine_decorator

# this router can both consume and send data
@coroutine_decorator
def router():
    try:
        while True:
            line = yield # consume data
            (first, last) = line.split(" ")
            fnames.send(first)  # send data to a coroutine
            lnames.send(last.strip()) # send data to another coroutine
    except GeneratorExit:
        fnames.close()
        lnames.close()
        
@coroutine_decorator
def file_write(filename):
    try:
        with open(filename, "a") as file:
            while True:
                line = yield
                file.write(line + "\n")    
    except GeneratorExit:
        file.close()
        print("a file has been created.")
        
        
        
if __name__ == "__main__":
    fnames = file_write("processed/first_names.txt")
    lnames = file_write("processed/last_names.txt")
    
    router = router()
    for name in open("data/names.txt"):
        router.send(name)
    router.close()