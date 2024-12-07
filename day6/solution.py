"""
Solving the maze, basic method:
** Part 1 **
* Determine starting position
* While not at edge of grid
* Calculate next position
* If next position is a space, move to next position, mark as visited
* If next position is a wall, rotate array, transform coordinate of current position
* Repeat until at edge of grid
* Count number of visited positions

** Part 2 **
* For each position in the grid, add an obstacle
* Repeat the navigation process
* Count the number of times an infinite loop is encountered
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
    # print(f"Rotating to {coord_current}")
    return ((array_limit[0] - 1) - coord_current[1]), coord_current[0]


def navigate_grid(coord_current: tuple[int, int], grid: np.array, max_steps: int = 50000) -> int:
    step_count = 0
    infinite_loop = 0
    array_limit = grid.shape
    grid[coord_current] = "x"  # mark the start position as visited

    while not edge_of_grid(coord_current, array_limit):

        coord_next = next_position(coord_current)

        if grid[coord_next] in ['.', 'x', '^']: # can move forward into any of these
            coord_current = coord_next
            grid[coord_current] = "x" # mark the position as visited
            step_count += 1

        else: # can't move forward, so rotate
            grid = np.rot90(grid) # rotate the grid counter-clockwise
            coord_current = rotate_coord(coord_current, array_limit)

        if step_count >= max_steps:
            print(f"{max_steps} steps reached, infinite loop likely")
            infinite_loop = 1
            break

    return infinite_loop

def count_visited(grid: np.array) -> int:
    count = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i,j] == "x":
                count += 1
    return count

def count_infinite_loops(grid):
    infinite_loop_count = 0
    grid_init = grid.copy()

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            grid = grid_init.copy()
            grid[i,j] = grid[i,j].replace('.', '#')
            # print(f'trying obstacle at grid[{i},{j}]')

            infinite_loop_count += navigate_grid(coord_current, grid)
            # print(f"inifinite loop count: {infinite_loop_count}")

    return infinite_loop_count

if __name__ == '__main__':

    ### Load data
    file_path = 'day6/input_data/input_test.txt'
    grid_master = load_data(file_path)
    grid = grid_master.copy()

    ### Part 1
    coord_current = find_start(grid) # initialise starting position
    navigate_grid(coord_current, grid)
    position_count = count_visited(grid)
    print(f"Unique positions visited: {position_count}")

    ### Part 2
    grid = grid_master.copy()
    coord_current = find_start(grid)  # initialise starting position
    infinite_loop_count = count_infinite_loops(grid) # this takes a couple of minutes for the full grid
    print(f"Number of infinite loops: {infinite_loop_count}")
