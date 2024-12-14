"""
Day 13
Used AI to parse the data into a list of tuples (regex & map).
Looked up how to rearrange the equations to solve for A and B using Cramer's rule.
"""

import re

# load data from text file
def load_data(file_path):
    with open(file_path) as file:
        data = file.read()
    return data


def parse_data(data):
    pattern = re.compile(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)")
    matches = pattern.findall(data)
    return matches


def is_whole_number(num):
    return num % 1 == 0


def too_many_presses(num):
    return num > 100


def solve_equations(machines: list, addition=0) -> int:
    running_total = 0

    for machine in machines:
        a_x, a_y, b_x, b_y, p_x, p_y = map(int, machine)

        p_x += addition
        p_y += addition

        # formulae solved for A and B (Cramer's rule)
        A = (p_x * b_y - p_y * b_x) / (a_x * b_y - a_y * b_x)
        B = (a_x * p_y - a_y * p_x) / (a_x * b_y - a_y * b_x)

        if not is_whole_number(A) or not is_whole_number(B):
            continue

        if addition == 0:
            if too_many_presses(A) or too_many_presses(B):
                continue

        running_total += ((A * 3) + B)
        # print(f"A: {A}, B: {B}, tokens: {running_total}")

    return int(running_total)


if __name__ == "__main__":
    data = load_data("day13/input_data/input_full.txt")
    machines = parse_data(data)

    total_pt1 = solve_equations(machines)
    print(f"Total tokens part 1: {total_pt1}")

    addition = 10000000000000
    total_pt2 = solve_equations(machines, addition)
    print(f"Total tokens part 2: {total_pt2}")
