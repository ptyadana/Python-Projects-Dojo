def fibonacci_generator(index):
    num1 = 0
    num2 = 1
    for i in range(index+1):
        yield num1
        total = num1 + num2
        num1 = num2
        num2 = total


for item in fibonacci_generator(20):
    print(item)