# https://adventofcode.com/2021/day/4
# Part1
# Write basic bingo game and count the score of winning board.

from pathlib import Path
import copy

script_parent = Path(__file__).parent
absolute_path = script_parent.resolve()
file_path = absolute_path / 'files' / 'day4.txt'

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
            board_row = [i.replace(' ', '  ').split() for i in board.split(sep='\n')]
            boards[index] = board_row
        return numbers, boards


def bingo(numbers, boards, part2=False):
    matched = {b:{i:[] for i in range(5)} for b in boards.keys()}
    matched_columns = {b:{i:[] for i in range(5)} for b in boards.keys()}
    part2_counter = {b:[] for b in boards.keys()}
    last_match_state = {}
    for number in numbers:
        print(number)
        for dict_key in boards.keys():
            board = boards.get(dict_key)
            for row_index, row_value in enumerate(board):
                if number in row_value:
                    matched_dict = matched[dict_key]
                    matched_dict.get(row_index).append(row_value.index(number))
                    matched_columns[dict_key][row_value.index(number)].append(1)
                    if len(matched_dict.get(row_index)) == 5:
                        part2_counter[dict_key].append(1)
                        if part2 is False:
                            print(f'Winning row in board {dict_key} row {row_index}: {matched_dict.get(row_index)}')
                            return number, matched[dict_key], boards.get(dict_key), 'row', row_index
                        else:
                            if len(part2_counter[dict_key]) <= 1:
                                last_number = number
                                last_match_state = copy.deepcopy(matched[dict_key])
                                print(f'Part2 unique winning state on board {dict_key}')
                                last_board = boards.get(dict_key)
                            else: pass
                    if len(matched_columns[dict_key][row_value.index(number)]) == 5:
                        part2_counter[dict_key].append(1)
                        if part2 is False:
                            print(f'Winning column in board {dict_key} column {row_value.index(number)}')
                            return number, matched[dict_key], boards.get(dict_key), 'column', row_value.index(number)
                        else:
                            if len(part2_counter[dict_key]) <= 1:
                                last_number = number
                                last_match_state = copy.deepcopy(matched[dict_key])
                                print(f'Part2 unique winning state on board {dict_key}')
                                last_board = boards.get(dict_key)
                            else: pass
                # Check if number in each row
                #   Create a dict of dicts to store the match data
                #   Save the match row_index, element_index, dict_key
                #   Increment number of match for row/element index
                #   If counter == 5
                #       return winner board
    return last_number, last_match_state, last_board


def board_score(win_number, matched, win_board):
    board = copy.deepcopy(win_board)
    for row_index in matched.keys():
        value = matched.get(row_index)
        for i in value:
            board[row_index][i] = 0
    board_sum = sum([sum([int(i) for i in row]) for row in board])
    score = board_sum * int(win_number)
    return score


numbers, boards = read_data(file_path)
win_number, matched, win_board, row_column, index = bingo(numbers, boards)
score = board_score(win_number, matched, win_board)
print(f'Board score is {score}')

# Part2
last_number, last_match_state, last_board = bingo(numbers, boards, part2=True)
part2_score = board_score(last_number, last_match_state, last_board)
print(f'Last board score is {part2_score}')