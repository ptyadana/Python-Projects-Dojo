def is_armstrong_number(num):
    original_num = num
    total = 0
    remainder = num % 10
    
    while remainder != 0:
        total += remainder ** 3
        num = num // 10
        remainder = num % 10
    
    return total == original_num



if __name__ == "__main__":
    print(is_armstrong_number(371))
    print(is_armstrong_number(123))
    print(is_armstrong_number(153))