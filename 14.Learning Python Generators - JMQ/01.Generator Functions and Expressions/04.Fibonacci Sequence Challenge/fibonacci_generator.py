def fibonacci_geneator(n):
    num1 = 0
    num2 = 1
    
    for i in range(n):
        if i == 0:
            yield num1
        elif i == 1:
            yield num2
        else:
            num1, num2 = num2, num1 + num2
            yield num2
            

if __name__ == "__main__":
    print(list(fibonacci_geneator(15)))
            