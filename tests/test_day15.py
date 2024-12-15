import numpy as np

from day15.solution import load_data, find_start_position, convert_command_to_direction, calculate_next_loc

def test_calc_next_loc():
    loc1 = (0, 0)
    loc2 = (1, 1)
    assert calculate_next_loc(loc1, loc2) == (1, 1)
    loc1 = (2, 2)
    loc2 = (-1, 0)
    assert calculate_next_loc(loc1, loc2) == (1, 2)


def test_find_start_position():
    grid = np.array([[".", ".", "."], [".", "@", "."], [".", "x", "."]])
    character = "@"
    assert find_start_position(grid, character) == (1, 1)
    character = "x"
    assert find_start_position(grid, character) == (2, 1)