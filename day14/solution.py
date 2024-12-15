"""
Day 14 - Part 1
"""

def load_data(file_path: str) -> list:
    with open(file_path, 'r') as f:
        return f.readlines()


def extract_values(data: str) -> tuple:
    parts = data.split(" ")
    pos = parts[0].split("=")[1].split(",")
    pos = (int(pos[0]), int(pos[1]))
    vel = parts[1].split("=")[1].split(",")
    vel = (int(vel[0]), int(vel[1]))
    return pos, vel


def move(p,v):
    return p[0]+v[0], p[1]+v[1]


def valid_pos(p: tuple, lim: tuple) -> tuple:
    """
    Calculates the wrapped position by taking the modulo of each coordinate with the corresponding limit.
    Ensures that if a coordinate exceeds the limit or is negative, it wraps around within the grid.
    """
    p_x = p[0] % lim[0]
    p_y = p[1] % lim[1]
    return (p_x, p_y)


def find_quadrant(pos: tuple, lim: tuple) -> int:
    x, y = pos
    w, h = lim
    w -= 1 # subtract 1 because the width is 1-based, but the position is 0-based
    h -= 1

    if x == w/2 or y == h/2:
        return 0 # on centre lines, doesn't count as a quadrant
    elif x < w/2 and y < h/2:
        return 1
    elif x > w/2 and y < h/2:
        return 2
    elif x < w/2 and y > h/2:
        return 3
    elif x > w/2 and y > h/2:
        return 4


def calc_product(result: dict) -> int:
    """
    Counts only the four quadrants containing robots.
    Accounts for no robots in quadrants.
    """
    result.pop(0) # remove the centre
    mult_store = []

    for value in result.values():
        if value != 0:
            mult_store.append(value)
    # multiply all in list
    if len(mult_store) == 0:
        return 0
    else:
        product = 1
        for value in mult_store:
            product *= value
        return product


def main_loop(data: list, lim: tuple, seconds: int) -> int:

    robot_count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}  # quadrant: no of robots

    robots = len(data)

    ### Main loop ###
    for index, line in enumerate(data):
        p, v = extract_values(data[index])

        print(f"robot {index} of {robots}: starting position {p}")

        for i in range(1, seconds + 1):
            new_p = move(p, v)
            val_p = valid_pos(new_p, lim)
            # print(f"after iteration {i}, position {val_p}")
            p = val_p

        quadrant = find_quadrant(p, lim)
        robot_count[quadrant] += 1
        print(f"final position {p}, is in quadrant {quadrant}")

    product = calc_product(robot_count)

    print(f"Quadrant count: {robot_count}")

    return product


if __name__ == "__main__":

    file_path = "day14/input_data/input_full.txt"
    data = load_data(file_path)
    lim = (101, 103)  # (width, height)
    seconds = 100
    product = main_loop(data, lim, seconds)
    print(f"Product of robots in quadrants: {product}")
