"""
Day 15 - Part 1

Method:
Load grid as numpy array
Convert each command to a direction
Check for boxes in the direction of the command until a space or wall is found
If a space is found move any boxes and the character
If a wall is found do nothing
In final grid, find location of all boxes, calculate GPS score
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
        commands = commands.replace("\n", "")
    return commands


def find_start_position(grid, character: str) -> tuple:
    start_loc = np.where(grid == character)
    start_loc = start_loc[0][0], start_loc[1][0] #convert to tuple
    return start_loc


def convert_command_to_direction(command: str) -> tuple:
    command_conversion = {
        "<": (0, -1),
        ">": (0, 1),
        "^": (-1, 0),
        "v": (1, 0)
    }
    return command_conversion[command]


def calculate_next_loc(loc1:tuple, loc2:tuple) -> tuple:
    return tuple(a + b for a, b in zip(loc1, loc2))


def calc_score(grid):
    boxes = np.where(grid == "O")
    score = boxes[0].sum() * 100 + boxes[1].sum()
    return score


if __name__ == "__main__":
    #Input grid
    file_path = "day15/input_data/input_grid_full.txt"
    grid = load_grid(file_path)

    #Input commands
    file_path = "day15/input_data/input_commands_full.txt"
    commands = load_commands(file_path)

    #Find start position
    character = "@"
    start_loc = find_start_position(grid, character)

    for index, command in enumerate(commands):
        print(f"Command: {index} of commands: {len(commands)}")

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
    score = calc_score(grid)
    print(f"GPS total {score}")