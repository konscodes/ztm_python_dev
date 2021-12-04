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
        numbers = data[0].split(sep=',')
        # Take list of boards as a str
        # Separate rows into separate values by \n
        # Turn str values into int lists
        boards = {}
        boards_list = data[1:]
        for index, board in enumerate(boards_list):
            #print(board)
            board_row = [i.replace(' ', '  ').split() for i in board.split(sep='\n')]
            boards[index] = board_row
        return numbers, boards


def bingo(numbers, boards):
    winner_board = {'index': 0, 'board': 0}
    matched = {b:{i:[] for i in range(5)} for b in boards.keys()}
    for number in numbers:
        print(number)
        for dict_key in boards.keys():
            board = boards.get(dict_key)
            for row_index, row in enumerate(board):
                if number in row:
                    matched_dict = matched[dict_key]
                    matched_dict.get(row_index).append(row.index(number))
                # Check if number in each row
                #   Create a dict of dicts to store the match data
                #   Save the match row_index, element_index, dict_key
                #   Increment number of match for row/element index
                #   If counter == 5
                #       set winner flag to True
                #       winner_board = dict_key 
        print(matched)
        # Check if winner exists
        # If winner is True return winner board
    return winner_board



numbers = read_data(file_path)[0]
boards = read_data(file_path)[1]

print(bingo(numbers, boards))