"""
Day 10: Parts 1 & 2
Method:
Scan grid for trailhead positions (0s)
For each trailhead: Initialise a dictionary to store found positions for each elevation
For each position in each elevation: Check neighbours for next elevation and add to found positions
For max elevation (9), count the number of paths (for part2) and the number of unique paths (for part1)
"""

import numpy as np

def load_data(file_path: str) -> np.array:
    input = np.loadtxt(file_path, dtype=str, comments=None)
    char_list = [list(line) for line in input] # split the lists into individual characters
    array = np.array(char_list, dtype=int)

    return array


def get_grid_limits(grid):

    return grid.shape[0] - 1


def find_trailhead_positions(grid, trailhead):
    trailhead_positions = np.column_stack(np.where(grid == trailhead))
    trailhead_positions = [tuple(map(int, x)) for x in trailhead_positions]

    return trailhead_positions


def calculate_neighbour_positions(position: tuple) -> list:
    i, j = position[0], position[1]

    return [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]


def validate_positions(positions, limit=9):

    return [position for position in positions if 0 <= position[0] <= limit and 0 <= position[1] <= limit]


def initialise_found_positions(max_number) -> dict:

    return {i: [] for i in range(max_number + 1)}


def calculate_paths(trailhead_positions: list, grid: np.array):
    """
    Main loop
    """

    limit = get_grid_limits(grid)
    max_elevation = 9  # dictated by puzzle rules

    total_paths = sum_of_ratings = 0 # initialise counters

    for trailhead in trailhead_positions:  # search trailhead
        found_positions = initialise_found_positions(max_elevation)
        found_positions[0] = [trailhead]

        for elevation in range(0, max_elevation +1):  # check elevations

            for position in found_positions[elevation]:  # check positions
                neighbour_positions = calculate_neighbour_positions(position)
                neighbour_positions = validate_positions(neighbour_positions, limit)

                next_elevation = elevation +1

                for position_to_check in neighbour_positions:  # check neighbours
                    if grid[position_to_check] == next_elevation:
                        found_positions[next_elevation].append(position_to_check)

        rating = len(found_positions[max_elevation])  # part2 requirement
        sum_of_ratings += rating

        unique_paths = set(found_positions[max_elevation])  # part1 requirement
        total_paths += len(unique_paths)

    return total_paths, sum_of_ratings


if __name__ == '__main__':
    file_path = 'day10/input_data/input_full.txt'
    grid = load_data(file_path)

    trailhead_positions = find_trailhead_positions(grid, 0) # find all trailheads
    total_paths, sum_of_ratings = calculate_paths(trailhead_positions, grid) # calculate paths from all trailheads

    print(f"Total paths: {total_paths}")
    print(f"Sum of ratings: {sum_of_ratings}")
