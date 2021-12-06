# Part1 and Part2 in one function

from pathlib import Path

path = Path(__file__).resolve()
parent = path.parent
file_path = parent / 'files' / 'day5.txt'

def read_data(file_path):
    with open(file_path) as file_object:
        data = file_object.read().replace(' -> ', ',').split(sep='\n')
        data = [[int(x) for x in i.split(sep=',')] for i in data]   
    return data


def build_matrix(vents):
    vents = vents.copy()
    size = max([max(i) for i in vents]) + 1
    matrix = [[0 for x in range(size)] for i in range(size)]
    return matrix


def mark_matrix(matrix, vents):
    new_matrix = matrix.copy()
    for line in vents:
        x1,y1,x2,y2 = line
        rows = sorted([y1,y2])
        columns = sorted([x1,x2])
        if x1 == x2:
            print(f'column {x1} to be marked in rows {y1, y2}')
            for i in range(rows[0],rows[1] + 1):
                new_matrix[i][x1] += 1
        elif y1 == y2:
            print(f'row {y1} to be marked in columns {x1, x2}')
            for i in range(columns[0],columns[1] + 1):
                new_matrix[y1][i] += 1
        else:
            print(f'rows {y1, y2} to be marked in columns {x1, x2}')
            x_counter = [i for i in range(columns[0],columns[1] + 1)]
            y_counter = [i for i in range(rows[0],rows[1] + 1)]
            if x1 < x2: x_counter.reverse()
            if y1 < y2: y_counter.reverse()
            for i in y_counter:
                j = x_counter.pop(0)
                new_matrix[i][j] += 1
    return new_matrix


vents = read_data(file_path)
matrix = build_matrix(vents)
new_matrix = mark_matrix(matrix, vents)
# [print(i) for i in new_matrix]
result = [[item >= 2 for item in row].count(True) for row in new_matrix]
print(f'At least 2 line overlap detected {sum(result)} times')