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
        data = data.split(sep='\n\n')
        numbers = [int(i) for i in data[0].split(sep=',')]
        # Take list of boards as a str
        # Separate rows into separate values by \n
        # Turn str values into int lists
        boards = {}
        boards_list = data[1:]
        for index, board in enumerate(boards_list):
            print(board)
            board_row = [i.replace(' ', '  ').split() for i in board.split(sep='\n')]
            boards[index] = board_row
        return numbers, boards


print(read_data(file_path))