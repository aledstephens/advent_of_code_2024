"""
Day 15 - Part 1
"""

import numpy as np

def load_grid(file_path: str) -> np.array:
    input = np.loadtxt(file_path, dtype=str, comments=None)
    char_list = [list(line) for line in input] # split the lists into individual characters
    array = np.array(char_list, dtype=str)
    return array


def load_commands(file_path: str) -> str:
    with open(file_path, "r") as file:
        commands = file.read()
        # remove new line characters
        commands = commands.replace("\n", "")
    return commands


def find_start_position(grid, character):
    start_loc = np.where(grid == character)
    start_loc = start_loc[0][0], start_loc[1][0] #convert to tuple
    return start_loc


def convert_command_to_direction(command):
    command_conversion = {
        "<": (0, -1),
        ">": (0, 1),
        "^": (-1, 0),
        "v": (1, 0)
    }
    return command_conversion[command]


def calculate_next_loc(loc1:tuple, loc2:tuple) -> tuple:
    return tuple(a + b for a, b in zip(loc1, loc2))

if __name__ == "__main__":
    #Input grid
    file_path = "day15/input_data/input_grid_full.txt"
    grid = load_grid(file_path)

    #Input commands
    file_path = "day15/input_data/input_commands_full.txt"
    commands = load_commands(file_path)

    character = "@"
    start_loc = find_start_position(grid, character)

    for command in commands:
        print(grid)
        print(command)

        move_direction = convert_command_to_direction(command)
        move_target = calculate_next_loc(start_loc, move_direction)

        # check for boxes
        box_list = []
        while grid[move_target] == "O":
            box_list.append(move_target)# add box to list to move
            move_target = calculate_next_loc(move_target, move_direction) #look at next location

        # can move
        if grid[move_target] == ".":
            # move boxes
            box_list.reverse() # working in backwards order
            for box in box_list:
                move_target = calculate_next_loc(box, move_direction)
                grid[move_target] = "O"

            # move character
            grid[start_loc] = "."
            move_target = calculate_next_loc(start_loc, move_direction)
            grid[move_target] = character
            start_loc = move_target

        # can't move
        else:
            continue

    # calculate score
    boxes = np.where(grid == "O")
    score = boxes[0].sum() * 100 + boxes[1].sum()
    print(f"GPS total {score}")


