def get_fibonacci_series(total_num):
    num1 = 0
    num2 = 1
    fib_list = [num1]
    
    for i in range(total_num - 1):
        
        total = num1 + num2
        num2 = num1
        num1 = total
        fib_list.append(total)
        
    return fib_list
        
if __name__ == "__main__":
    how_many = int(input("How many fibonacci numbers? "))
    print(get_fibonacci_series(how_many))    

    