# Part1
from pathlib import Path
import matplotlib.pyplot as plt

path = Path(__file__).resolve()
parent = path.parent
file_path = parent / 'files' / 'test7.txt'

def read_data(file_path):
    with open(file_path) as file_object:
        data = file_object.read().split(sep=',')
        data = [int(i) for i in data]
    return data


def plotme(data: list, path):
    data = [23,85, 72, 43, 52]
    labels = ['A', 'B', 'C', 'D', 'E']
    plt.xticks(range(len(data)), labels)
    plt.xlabel('Class')
    plt.ylabel('Amounts')
    plt.title('I am title')
    plt.bar(range(len(data)), data) 
    plt.savefig('plot.png')


# def moving_cost(position: int, in_range):
#     return cost_distribution

#def distance_between_elements(position: int, in_range)

data = read_data(file_path)
available_space = [0 for i in range(max(data) + 1)]
print(available_space)

# Data - horizontal positions
# Range of the data is max position
# For each positions get the distance between distance_between_elements
# Apply factorial for each distance in the range to get total cost cost_distribution
# Merge cost distribution for each position to get superposition of cost_distribution
# Minimum value index will be our position to allign to. Well total cost is already there as well