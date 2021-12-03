# Part1
# Find the most common and the least common bit sequence.
# Multiply least common decimal to most common decimal.
# In example data, gamma rate is the binary number 10110, or 22 in decimal.
# The epsilon rate is 01001, or 9 in decimal. 
# Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

from pathlib import Path

script_path = Path(__file__).resolve()
script_parent = script_path.parent
data_file_path = script_parent / 'files' / 'day3.txt'

def read_data(file_path):
    with open(file_path) as file_object:
        data = file_object.read()
        data = data.split(sep='\n')
    return data


def get_transposed_data(data: list):
    keydict = {}
    data = data.copy()
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
    binary = binary.copy()
    for i in range(len(binary)):
        digit = binary.pop()
        if digit == 1:
            decimal = decimal + pow(2, i)
    return decimal


data_list = read_data(data_file_path)
data_transposed = get_transposed_data(data_list)
common_value = find_common(data_transposed)
gamma = convert_to_decimal(common_value[0])
epsilon = convert_to_decimal(common_value[1])
print(f'Gamma rate is {gamma} and epsilon rate is {epsilon}')
print(f'Power consumption is {gamma * epsilon}')


# Part2
# https://adventofcode.com/2021/day/3#part2

def check_func(index_to_check, bit_sequence, number_list, type):
    if type == 'Oxygen':
        if bit_sequence.count('1') > bit_sequence.count('0'):
            filtered_list = [item for item in number_list if item[index_to_check] == '1']
        elif bit_sequence.count('0') > bit_sequence.count('1'):
            filtered_list = [item for item in number_list if item[index_to_check] == '0']
        else:
            filtered_list = [item for item in number_list if item[index_to_check] == '1']
    else:
        if bit_sequence.count('1') > bit_sequence.count('0'):
            filtered_list = [item for item in number_list if item[index_to_check] == '0']
        elif bit_sequence.count('0') > bit_sequence.count('1'):
            filtered_list = [item for item in number_list if item[index_to_check] == '1']
        else:
            filtered_list = [item for item in number_list if item[index_to_check] == '0']
    return filtered_list


def filter_func(data_list, type):
    result = data_list.copy()
    data_transposed = get_transposed_data(result)
    for index, value in enumerate(data_list):
        try:
            result = check_func(index, data_transposed[index], result, type)
            data_transposed = get_transposed_data(result)
            if len(result) == 1:
                break
        except KeyError as err:
            print('Key error at ', err)
    return result


oxygen_binary = filter_func(data_list, 'Oxygen')
oxygen_binary = [[int(i) for i in item] for item in oxygen_binary]
oxygen = convert_to_decimal(oxygen_binary[0])
co2_binary = filter_func(data_list, 'CO2')
co2_binary = [[int(i) for i in item] for item in co2_binary]
co2 = convert_to_decimal(co2_binary[0])
print(f'Oxygen is {oxygen} and CO2 is {co2}')
print(f'Life support rating is {oxygen * co2}')