# Part 1
# Calculate the horizontal position and depth you would have after following the planned course. 
# What do you get if you multiply your final horizontal position by your final depth?
# In test2.txt example, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)
# 
# Part 2
# Add aim to the challenge
# In test2.txt example, you would have a horizontal position of 15 and a depth of 60. (Multiplying these produces 900.)

from pathlib import Path

script_path = Path(__file__).resolve()
script_parent = script_path.parent
data_file_path = script_parent / 'files' / 'day2.txt'

def read_data(file_path):
    with open(file_path) as file_object:
        data = file_object.read()
        data = data.split(sep='\n')
        data_list = [i.split(sep=' ') for i in data]
    return data_list


def part1(data_list):
    data_dict = {'forward':0, 'down':0, 'up':0, 'depth':0, 'position':0}
    for item in data_list:
        key, value = item[0], int(item[1])
        data_dict[key] = data_dict.get(key) + value
    data_dict['depth'] = data_dict['down'] - data_dict['up']
    data_dict['position'] = data_dict['forward'] * data_dict['depth']
    return data_dict


def part2(data_list):
    data_dict = {'forward':0, 'down':0, 'up':0, 'depth':0, 'position':0, 'aim':0}
    for item in data_list:
        key, value = item[0], int(item[1])
        data_dict[key] = data_dict.get(key) + value
        if key == 'down':
            data_dict['aim'] = data_dict.get('aim') + value
        elif key == 'up':
            data_dict['aim'] = data_dict.get('aim') - value
        else:
            data_dict['depth'] = data_dict.get('depth') + (data_dict.get('aim') * value)
    data_dict['position'] = data_dict['forward'] * data_dict['depth']
    return data_dict

data = read_data(data_file_path)
result1 = part1(data)
result2 = part2(data)
print(f'Part1 coordinates: {result1["position"]}')
print(f'Part2 coordinates: {result2["position"]}')
