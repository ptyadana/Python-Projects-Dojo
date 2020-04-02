#decorator of checking how long a certain function took in seconds
from time import time

def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} seconds')
        return result
    return wrapper

@performance
def long_time():
    for i in range(0,1000000):
        i*5

long_time()