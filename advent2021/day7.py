# Part1
from pathlib import Path
import statistics

path = Path(__file__).resolve()
parent = path.parent
file_path = parent / 'files' / 'day7.txt'

def read_data(file_path):
    with open(file_path) as file_object:
        data = file_object.read().split(sep=',')
        data = [int(i) for i in data]
    return data

# Working but only with test data
def first_try(data):
    horizontal = data.copy()
    counter = [0 for x in range(max(horizontal)+1)]
    for i in horizontal:
        counter[i] += 1
    start = 0
    end = len(counter)
    position = round((start + end) / 2)
    while position > 2:
        position = round((start + end) / 2)
        if sum(counter[start:position]) > sum(counter[position:end]):
            end = position
        else: start = position
    fuel = 0
    for i in horizontal:
        fuel += abs(i - position)
    return fuel

# Not working just like this, need to add mode and median to compare
def simple_mean(data):
    horizontal = data.copy()
    mean = sum(horizontal) / len(horizontal)
    print(mean, int(mean))
    fuel = sum([abs(int(mean) - i) for i in horizontal])
    return fuel


def easy_way(data):
    pos = data.copy()
    mean = statistics.mean(pos)
    median = statistics.median(pos)
    mode = statistics.mode(pos)
    possible_best = mean, median, mode
    print(possible_best)
    fuel = [sum([abs(x - int(i)) for x in pos]) for i in possible_best]
    return fuel


data = read_data(file_path)
result = easy_way(data)
print(f'Best distance is {min(result)}')
