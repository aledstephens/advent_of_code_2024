import numpy as np

from day10.solution import find_trailhead_positions, calculate_neighbour_positions, validate_positions, initialise_found_positions

def test_find_trailhead_positions():
    grid = np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
    trailhead = 0
    expected = [(0, 2), (1, 1), (2, 0)]
    assert find_trailhead_positions(grid, trailhead) == expected

def test_calc_neighbour_positions():
    position = (1, 1)
    expected = [(0, 1), (1, 2), (2, 1), (1, 0)]
    assert calculate_neighbour_positions(position) == expected

def test_validate_positions():
    positions = [(0,0), (0, -1), (11, 2), (-2, -1), (12, 13)]
    expected = [(0, 0)]
    assert validate_positions(positions, limit=10) == expected

def test_initialise_found_positions():
    expected = {0: [], 1: [], 2: [], 3: [], 4: []}
    assert initialise_found_positions(max_number=4) == expected