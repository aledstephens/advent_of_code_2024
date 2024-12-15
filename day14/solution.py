"""
Day 14

Part 1: Safety score
For each robot record final position
Calculate which quadrant each robot is in
Count number of robots in each quadrant

Part 2: Xmas tree
Store location of each robot each second
Calculate which quadrant each robot is in each second
Visually find when robots cluster in a single quadrant (for me it was Q4 after 6377)
"""

import pandas as pd
import plotly.express as px

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


def move(p: tuple,v: tuple) -> tuple:
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

    location_store = {} # used for part 2

    robot_count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}  # quadrant: no of robots

    robots = len(data)

    ### Main loop ###
    for index, line in enumerate(data): # each robot
        p, v = extract_values(data[index])
        location_store[index] = [p]

        print(f"robot {index} of {robots}: starting position {p}")

        for i in range(1, seconds + 1):
            new_p = move(p, v)
            val_p = valid_pos(new_p, lim)
            # print(f"after iteration {i}, position {val_p}")
            p = val_p
            location_store[index].append(p)

        quadrant = find_quadrant(p, lim)
        robot_count[quadrant] += 1
        print(f"final position {p}, is in quadrant {quadrant}")

    product = calc_product(robot_count)

    print(f"Quadrant count: {robot_count}")

    return product, location_store


def find_quadrants_all_robots(location_store: dict, lim: tuple) -> pd.DataFrame:
    """
    For each robot, calculate the quadrant it is in for each second.
    """

    quad_store = {}

    for index, data in location_store.items():
        quad_store[index] = []
        for pos in data:
            quad = find_quadrant(pos, lim)
            quad_store[index].append(quad)

    df = pd.DataFrame(quad_store)

    # for each row count the number of robots in each quadrant
    df["quad1"] = df.apply(lambda row: row.value_counts().get(1, 0), axis=1)
    df["quad2"] = df.apply(lambda row: row.value_counts().get(2, 0), axis=1)
    df["quad3"] = df.apply(lambda row: row.value_counts().get(3, 0), axis=1)
    df["quad4"] = df.apply(lambda row: row.value_counts().get(4, 0), axis=1)

    return df


def plot_quadrants(df: pd.DataFrame):
    """
    Plot the number of robots in each quadrant over time.
    """
    fig = px.scatter(df, y=["quad1", "quad2", "quad3", "quad4"], title="Number of robots in each quadrant over time")
    fig.update_layout(
        xaxis_title="Seconds",
        yaxis_title="Robots in quadrant",
        legend_title="Quadrant no.",
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="RebeccaPurple"),
        plot_bgcolor='white'
    )

    fig.show()


if __name__ == "__main__":

    ### Part 1
    file_path = "day14/input_data/input_full.txt"
    data = load_data(file_path)
    lim = (101, 103)  # (width, height)
    seconds = 8000
    product, location_store = main_loop(data, lim, seconds)
    print(f"Product of robots in quadrants: {product}")

    ### Part 2
    df = find_quadrants_all_robots(location_store, lim)
    plot_quadrants(df)
    # stats show grouping into a single quadrant
    df[['quad1', 'quad2', 'quad3', 'quad4']].max()
    df[['quad1', 'quad2', 'quad3', 'quad4']].idxmax()