# Count the number of times a depth measurement increases from the previous measurement.
# In test.txt example, there are 7 measurements that are larger than the previous measurement.

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
    decreased_counter = 0
    for current_item in list_of_int:
        if current_item > previous_item:
            increased_counter += 1
            previous_item = current_item
        elif current_item < previous_item:
            decreased_counter += 1
            previous_item = current_item
        else: 
            previous_item = current_item
    return increased_counter, decreased_counter

measurements = read_data(data_file_path)
result = compare_data(measurements)
print(f'Measurement increased {result[0]} times')