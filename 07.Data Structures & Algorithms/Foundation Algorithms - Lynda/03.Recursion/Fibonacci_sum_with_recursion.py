def get_fibonacci_sum(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return get_fibonacci_sum(n-1)+get_fibonacci_sum(n-2)
    
if __name__ == "__main__":
    print(get_fibonacci_sum(10))