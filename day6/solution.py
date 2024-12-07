"""
Solving the maze, basic method:
* Determine starting position
* While not at edge of grid
* Calculate next position
* If next position is a space, move to next position, mark as visited
* If next position is a wall, rotate array, transform coordinate of current position
* Repeat until at edge of grid
* Count number of visited positions
"""

# load as numpy array
import numpy as np

def load_data(file_path: str) -> np.array:
    input = np.loadtxt(file_path, dtype=str, comments=None)
    char_list = [list(line) for line in input] # split the lists into individual characters
    array = np.array(char_list)
    return array


def find_start(input: np.array) -> tuple[int, int]:
    for i in range(input.shape[0]):
        for j in range(input.shape[1]):
            if input[i,j] == '^':
                return i,j


def edge_of_grid(coord: tuple[int, int], array_limit: tuple[int, int]) -> bool:
    max_coord = (array_limit[0] - 1, array_limit[1] - 1)
    return coord[0] == 0 or coord[0] == max_coord[0] or coord[1] == 0 or coord[1] == max_coord[1]


def next_position(coord_current: tuple[int, int]) -> tuple[int, int]:
    coord_next = (coord_current[0] - 1, coord_current[1])
    return coord_next


def rotate_coord(coord_current: tuple[int, int], array_limit: tuple[int, int]) -> tuple[int, int]:
    print(f"Rotating to {coord_current}")
    return ((array_limit[0] - 1) - coord_current[1]), coord_current[0]


def navigate_grid(coord_current: tuple[int, int], grid: np.array):
    array_limit = grid.shape
    grid[coord_current] = "x"  # mark the start position as visited

    while not edge_of_grid(coord_current, array_limit):

        coord_next = next_position(coord_current)

        if grid[coord_next] in ['.', 'x', '^']: # can move forward into any of these
            coord_current = coord_next
            grid[coord_current] = "x" # mark the position as visited

        else: # can't move forward, so rotate
            grid = np.rot90(grid) # rotate the grid counter-clockwise
            coord_current = rotate_coord(coord_current, array_limit)

def count_visited(grid: np.array) -> int:
    count = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i,j] == "x":
                count += 1
    return count

file_path = 'day6/input_data/input_full.txt'
grid = load_data(file_path)

coord_current = find_start(grid) # initialise starting position
navigate_grid(coord_current, grid)
position_count = count_visited(grid)
print(f"Unique positions visited: {position_count}")
