# Find the greatest common denominator of two numbers
# using Eculid's algorithms

def get_gcd(a, b):

    while b != 0:
        temp = a
        a = b
        b = temp % b
    
    return a

if __name__ == "__main__":
    print("Greatest Common Denominator: ", get_gcd(20, 8))
    print("Greatest Common Denominator: ", get_gcd(60, 96))