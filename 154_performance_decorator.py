# Performance decorator
from time import time

def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Runtime is {round(t2 - t1, 2)}s')
        return result
    return wrapper

@performance
def long_time():
    for i in range(10000000):
        i*5

long_time()