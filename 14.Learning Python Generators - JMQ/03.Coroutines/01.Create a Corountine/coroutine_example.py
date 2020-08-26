def coroutine_example():
    while True:
        x = yield
        # do something
        print(x)
        
        


if __name__ == "__main__":
    c = coroutine_example()
    c.__next__()
    c.send(10)