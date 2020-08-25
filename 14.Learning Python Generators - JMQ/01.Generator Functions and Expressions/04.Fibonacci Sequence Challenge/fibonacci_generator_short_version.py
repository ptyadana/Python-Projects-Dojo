def fibonacci_geneator():
    trailing, lead = 0, 1
    while True:
        yield lead
        trailing, lead = lead, trailing+lead
        
        
        
if __name__ == "__main__":
    fib = fibonacci_geneator()
    
    for item in range(15):
        print(fib.__next__())