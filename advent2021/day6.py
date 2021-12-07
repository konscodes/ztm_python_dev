# Part1 
# Part2 Performance decorator
# Part2 speed issues with list.append() 
# resolved by droping append in favor of different approach counting sum of increments for each newly created number.
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
def slow_loop(data):
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


@performance
def faster_loop(data):
    fish = data.copy()
    days = 60
    for day in range(days):
        new_fish = []
        for i, value in enumerate(fish):
            if value == 0:
                fish[i] = 6
                new_fish.append(8)
            elif 7 <= value <= 8:
                fish[i] -= 1
            else: 
                fish[i] -= 1
            #print(day, i, state, counter)
        fish.extend(new_fish)
    return fish


@performance
# Solution from
# https://github.com/wmporter/aoc2021/blob/main/day/6/part2.py
def the_fastest(data):
    fish = data.copy()
    days = 256
    fish_added = [0] * days
    # Instead of manipulating list of fish, we only increment all newly created fish
    # Fish created from initial list
    for f in fish:
        fish_added[f] += 1
        for i in range(f+7, days, 7):
            fish_added[i] += 1
    # Fish created from newly born fish thus + 2 days with step of 7 days
    for day in range(days):
        for d in range(day+9, days, 7):
            fish_added[d] += fish_added[day]
    return fish_added


data = read_data(file_path)
result1 = slow_loop(data)
result2 = faster_loop(data)
result3 = the_fastest(data)
print(f'Total {len(result1)} fish')
print(f'Total {len(result2)} fish')
print(f'Total {sum(result3) + len(data)} fish')