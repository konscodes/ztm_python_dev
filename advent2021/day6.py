# Part1 
# Part2 Performance decorator
from time import time
from pathlib import Path

path = Path(__file__).resolve()
parent = path.parent
file_path = parent / 'files' / 'day6.txt'

def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Runtime is {round(t2 - t1, 2)}s')
        return result
    return wrapper


def read_data(file_path):
    with open(file_path) as file_object:
        data = file_object.read().split(sep=',')
        data = [int(i) for i in data]
    return data

@performance
def main_loop(data):
    counter = data.copy()
    days = 60
    for day in range(days):
        for i in counter.copy():
            state = counter.pop(0)
            if state == 0:
                counter.append(6)
                counter.append(8)
            elif 7 <= state <= 8:
                counter.append(state - 1)
            else: 
                counter.append(state - 1)
            #print(day, i, state, counter)
    return counter


data = read_data(file_path)
result = main_loop(data)
print(f'Total {len(result)} fish')