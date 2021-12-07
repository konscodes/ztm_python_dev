# Part1
from pathlib import Path

path = Path(__file__).resolve()
parent = path.parent
file_path = parent / 'files' / 'day7.txt'

def read_data(file_path):
    with open(file_path) as file_object:
        data = file_object.read().split(sep=',')
        data = [int(i) for i in data]
    return data


def selection(data):
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

data = read_data(file_path)
result = selection(data)
print(result)