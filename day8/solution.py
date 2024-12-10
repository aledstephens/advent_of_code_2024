'''
1. for an antenna get the distance to every other antenna
2. add those distances to that antenna to get antinode positions
3. keep only antinodes in grid and remove duplicates
'''

# load as numpy array
import numpy as np

def load_data(file_path: str) -> np.array:
    input = np.loadtxt(file_path, dtype=str, comments=None)
    char_list = [list(line) for line in input] # split the lists into individual characters
    array = np.array(char_list)
    return array

def setup_antennae() -> str:
    antennae = 'abcdefghijklmnopqrstuvwxyz'
    antennae += antennae.upper()
    antennae += '0123456789'
    return antennae


def subtract_tuples(tuple1, tuple2):
    return tuple(a - b for a, b in zip(tuple1, tuple2))


def add_tuples(tuple1, tuple2):
    return tuple(a + b for a, b in zip(tuple1, tuple2))


def find_antenna_positions(grid, antenna):
    antenna_positions = np.column_stack(np.where(grid == antenna))
    antenna_positions = [tuple(map(int, x)) for x in antenna_positions]

    return antenna_positions


def remove_invalid_positions(tuple_list, max):
    lst =  [t for t in tuple_list if 0 <= t[0] <= max and 0 <= t[1] <= max]
    return list(set(lst))

if __name__ == '__main__':

    ### Load data
    file_path = 'day8/input_data/input_test.txt'
    grid = load_data(file_path)

    antennae = setup_antennae()

    antinode_position_store = []

    for antenna in antennae:
        print(f"antenna: {antenna}")

        # find all antenna positions
        antenna_positions = find_antenna_positions(grid, antenna)
        print(f"antenna position: {antenna_positions}")

        # for each pair of antenna positions, calculate the distance, and add to the original position
        for i in antenna_positions:
            print(f"Position: {i}")
            distances = [subtract_tuples(i, j) for j in antenna_positions]
            distances = [x for x in distances if x != (0,0)] # remove the antenna position itself
            print(f"Distances: {distances}")

            antinode_positions = [add_tuples(i,j) for j in distances]
            print(f"antinodes at: {antinode_positions}")
            antinode_position_store.extend(antinode_positions) # add to the store

    antinode_position_store = remove_invalid_positions(antinode_position_store, len(grid)-1)
    print(f"Number of antinodes: {len(antinode_position_store)}")
