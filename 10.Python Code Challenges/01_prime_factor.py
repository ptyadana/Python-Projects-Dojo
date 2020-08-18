"""
Input: Integer
Output: list of prime factor
Example: get_prime_factors(630) returns [2,3,3,5,7]
Example: get_prime_factors(13) returns [13]
"""

def get_prime_factors(num):
    factors = []
    divisor = 2

    while divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
            num = num / divisor
        else:
            divisor += 1
    return factors


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    p_factors = get_prime_factors(number)
    print("The Prime Factors are : ", p_factors)