# Part1
# Find the most common and the least common bit sequence.
# Multiply least common decimal to most common decimal.
# In example data, gamma rate is the binary number 10110, or 22 in decimal.
# The epsilon rate is 01001, or 9 in decimal. 
# Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

from pathlib import Path

script_path = Path(__file__).resolve()
script_parent = script_path.parent
data_file_path = script_parent / 'files' / 'test3.txt'

def read_data(file_path):
    with open(file_path) as file_object:
        data = file_object.read()
        data = data.split(sep='\n')
    return data


def get_transposed_data(data: list):
    keydict = {}
    for i in range(len(data[0])):
        keydict[i] = []
    for line in data:
        for index, value in enumerate(line):
            keydict[index].append(value)
    return keydict


def find_common(data: dict):
    most_common = []
    least_common = []
    for values_list in data.values():
        if values_list.count('0') > values_list.count('1'):
            most_common.append(0)
            least_common.append(1)
        else:
            most_common.append(1)
            least_common.append(0)
    return most_common, least_common


def convert_to_decimal(binary: list):
    decimal = 0
    for i in range(len(binary)):
        digit = binary.pop()
        if digit == 1:
            decimal = decimal + pow(2, i)
    return decimal


data_list = read_data(data_file_path)
data_transposed = get_transposed_data(data_list)
common_value = find_common(data_transposed)
gamma = convert_to_decimal(common_value[0])
elipson = convert_to_decimal(common_value[1])
print(f'Gamma rate is {gamma} and elipson rate is {elipson}')
print(f'Power consumption is {gamma * elipson}')