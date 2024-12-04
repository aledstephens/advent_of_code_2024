'''
Solving the X-MAS
'''

# load as numpy array
import numpy as np

def load_data(file_path: str) -> np.array:
    input = np.loadtxt(file_path, dtype=str)
    char_list = [list(line) for line in input] # split the lists into individual characters
    array = np.array(char_list)
    return array


def search_for_char(input: np.array, char_to_find: str) -> list[tuple[int,int]]:
    result = []
    for i in range(input.shape[0]):
        for j in range(input.shape[1]):
            if input[i,j] == char_to_find:
                result.append((i,j))
    return result


def find_valid_diag_neighbours(coord: tuple[int, int], array_limit: tuple[int, int]) -> list[tuple[int, int]]:
    nbr_all = [
        (coord[0] - 1, coord[1] -1), # top left
        (coord[0] + 1, coord[1] + 1), # bottom right
        (coord[0] - 1, coord[1] + 1), # top right
        (coord[0] + 1, coord[1] - 1), # bottom left
    ] # returns coord neighbours, diagonals

    limit = (array_limit[0], array_limit[1])

    nbr_valid = []

    for coord in nbr_all:
        if check_bounds(coord, limit) == False:
            nbr_valid.append(coord)

    return nbr_valid


def check_bounds(coord: tuple[int, int], array_limit: tuple[int, int]) -> bool:
    return coord[0] < 0 or coord[0] > array_limit[0] or coord[1] < 0 or coord[1] > array_limit[1]


def check_diags(char_lst):
    if "M" in char_lst[:2] and "S" in char_lst[:2]: # top left and bottom right
        if "M" in char_lst[2:] and "S" in char_lst[2:]: # bottom right and top left
            print(f'found X-MAS')
            return True
    return False

def find_x_mas(A_loc: list[tuple[int, int]], input: np.array) -> int:
    x_mas_count = 0

    array_limit = input.shape
    array_limit = (array_limit[0] - 1, array_limit[1] - 1)

    for curr_A in A_loc:
        nbr_coords = find_valid_diag_neighbours(curr_A, array_limit)

        if len(nbr_coords) < 4: # discount character on edge
            continue

        print(f'valid A at {curr_A}')
        char_lst = []

        for coord in nbr_coords:
            char_lst.append(input[coord])

        if check_diags(char_lst):
                x_mas_count += 1

    return x_mas_count


file_path = 'day4/input_data/full-input.txt'
input = load_data(file_path)

char_locs = search_for_char(input, 'A') # list coords of all 'A' in the data
x_mas_count = find_x_mas(char_locs, input)
print(f'!!! X-MAS count: {x_mas_count} !!!')






