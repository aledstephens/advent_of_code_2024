'''
Solving the wordsearch
'''

# load as numpy array
import numpy as np

def load_data(file_path: str) -> np.array:
    input = np.loadtxt(file_path, dtype=str)
    char_list = [list(line) for line in input] # split the lists into individual characters
    array = np.array(char_list)
    return array


def search_for_X(input: np.array) -> list[tuple[int,int]]:
    result = []
    for i in range(input.shape[0]):
        for j in range(input.shape[1]):
            if input[i,j] == 'X':
                result.append((i,j))
    return result


def find_valid_neighbours(coord: tuple[int, int], array_limit: tuple[int, int]) -> list[tuple[int, int]]:
    nbr_all = [
        (coord[0] - 1, coord[1] -1),
        (coord[0] - 1, coord[1]    ),
        (coord[0] - 1, coord[1] + 1),
        (coord[0],     coord[1] - 1),
        (coord[0],     coord[1] + 1),
        (coord[0] + 1, coord[1] - 1),
        (coord[0] + 1, coord[1]    ),
        (coord[0] + 1, coord[1] + 1),
    ] # returns coord neighbours

    limit = (array_limit[0], array_limit[1])

    nbr_valid = [
        neighbour for neighbour in nbr_all
        if 0 <= neighbour[0] <= limit[0]
           and 0 <= neighbour[1] <= limit[1]
    ]

    return nbr_valid


def check_bounds(coord: tuple[int, int], array_limit: tuple[int, int]) -> bool:
    return coord[0] < 0 or coord[0] > array_limit[0] or coord[1] < 0 or coord[1] > array_limit[1]


def find_xmas(X_loc: list[tuple[int, int]], input: np.array) -> int:
    xmas_count = 0

    array_limit = input.shape
    array_limit = (array_limit[0] - 1, array_limit[1] - 1)

    for curr_X in X_loc:
        print(f'Checking X at {curr_X}')

        # get coords of neighbours and filter invalid locations
        nbr_coords = find_valid_neighbours(curr_X, array_limit)
        # print(f'neighbours of {curr_X} are: {nbr_coords}')

        # check which are 'M'
        for check_M in nbr_coords:

            if input[check_M] == 'M':
                print(f'found M at {check_M}')

                diff_x = check_M[0] - curr_X[0]
                diff_y = check_M[1] - curr_X[1]
                check_A = ((check_M[0] + diff_x), (check_M[1] + diff_y))

                if check_bounds(check_A, array_limit):
                    continue

                if input[check_A] == 'A':
                    print(f'found A at {check_A}')
                    check_S = ((check_A[0] + diff_x), (check_A[1] + diff_y))

                    if check_bounds(check_S, array_limit):
                        continue

                    if input[check_S] == 'S':
                        print(f'found S at {check_S}')
                        print(f'Found XMAS')
                        xmas_count += 1
    return xmas_count


file_path = 'day4/input_data/full-input.txt'
input = load_data(file_path)

X_loc = search_for_X(input) # list coords of all 'X' in the data
xmas_count = find_xmas(X_loc, input)

print(f'!!! XMAS count: {xmas_count} !!!')