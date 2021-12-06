# Part1

from pathlib import Path

path = Path(__file__).resolve()
parent = path.parent
file_path = parent / 'files' / 'test5.txt'

def read_data(file_path):
    with open(file_path) as file_object:
        data = file_object.read().replace(' -> ', ',').split(sep='\n')
        data = [[int(x) for x in i.split(sep=',')] for i in data]   
    return data


def build_matrix(vents):
    vents = vents.copy()
    size = max([max(i) for i in vents])
    matrix = [[0] * size] * size
    return matrix


def mark_matrix(matrix, vents):
    new_matrix = matrix.copy()
    for line in vents:
        x1,y1,x2,y2 = line
        if x1 == x2:
            print(f'column {x1} to be marked in rows {y1, y2}')
            rows = sorted([y1,y2])
            for i in range(rows[0],rows[1]):
                print(i)
                new_matrix[i][x1] += 1
                print(new_matrix)

vents = read_data(file_path)
matrix = build_matrix(vents)
mark_matrix(matrix, vents)