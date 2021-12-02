# Part 1
# Count the number of times a depth measurement increases from the previous measurement.
# In test.txt example, there are 7 measurements that are larger than the previous measurement.
# 
# Part 2
# Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum.
# In test.txt example, there are 5 sums that are larger than the previous sum.

from pathlib import Path

script_path = Path(__file__).resolve()
script_parent = script_path.parent
data_file_path = script_parent / 'files' / 'day1.txt'

def read_data(file_path):
    with open(file_path) as file_object:
        data = file_object.read()
        data_list = data.split()
        data_list = list(map(lambda i:int(i), data_list))
    return data_list


def compare_data(list_of_int):
    previous_item = list_of_int[0]
    increased_counter = 0 
    for current_item in list_of_int:
        if current_item > previous_item:
            increased_counter += 1
        previous_item = current_item
    return increased_counter


def compare_sliding_window(list_of_int, window_size=3): 
    increased_counter = 0
    previous_sum = sum(list_of_int[:3])
    for index, item in enumerate(list_of_int):
        if index >= 2:
            last_three_index = [index-x for x in range(window_size)]
            last_three_items = [list_of_int[y] for y in last_three_index]
            current_sum = sum(last_three_items)
            if current_sum > previous_sum:
                increased_counter += 1
            previous_sum = current_sum
    return increased_counter


measurements = read_data(data_file_path)

result1 = compare_data(measurements)
print(f'Measurement increased {result1} times')

result2 = compare_sliding_window(measurements)
print(f'Measurement increased {result2} times using sliding window method')