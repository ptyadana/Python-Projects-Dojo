"""
Input: Integer
Output: True for prime, False for not prime
"""

def is_prime(num):
    prime = False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime = True
    return prime

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print("It is a prime number." if is_prime(number) else "It is NOT a prime number.")