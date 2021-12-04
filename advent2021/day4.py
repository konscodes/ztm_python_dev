# https://adventofcode.com/2021/day/4
# Part1
# Write basic bingo game and count the score of winning board.

from pathlib import Path

script_parent = Path(__file__).parent
absolute_path = script_parent.resolve()
file_path = absolute_path / 'files' / 'test4.txt'

def read_data(file_path):
    with open(file_path) as file_object:
        data = file_object.read()
        print(data)


read_data(file_path)