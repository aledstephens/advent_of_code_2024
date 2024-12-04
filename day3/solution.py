"""
For part 2, the method is:
* split on don't() to get a list,
* split those lists on do(),
* ignore the first element of each sub-list
* but always keep the first list
"""

import re

def extract_mul(data: str) -> list[tuple[str,str]]:
    """
    Match this pattern: mul(X,Y) where X and Y are numbers
    """

    pattern = r'mul\((\d+),(\d+)\)' # r is for raw string, \d is for digits, + is for 1 or more

    match_lst = re.findall(pattern, data)

    return match_lst


def mul_tuples_and_sum(data: list[tuple[str,str]]) -> int:
    """
    Multiply the tuples and return the sum
    """
    total = []
    for tup in data:
        total.append(int(tup[0]) * int(tup[1]))
    total = sum(total)
    return total


def split_str_on_dont(data: str) -> list[str]:
    split_string = data.split("don't()")
    return split_string


def split_str_on_do(data: list[str]) -> list[list[str]]:
    total = []
    for item in data:
        split_string = item.split("do()")
        total.append(split_string)
    return total


def remove_invalid_items(split_string: list[str]) -> list[str]:
    total = []
    for index, element in enumerate(split_string):
        if index == 0:  # always store first element
            total.append(element)
        elif len(element) > 1:  # longer elements have a do() so ignore first part
            total.append(element[1:])
        else:  # single elements are only a dont() so ignore
            continue

    return total


if __name__ == "__main__":

    #Import data
    file_path = 'day3/input_data/input_data.txt'
    input_data = open(file_path, "r").read()

    #Solution to Part 1
    matches = extract_mul(input_data)
    result = mul_tuples_and_sum(matches)

    print(f'Pt1, sum of muls: {result}')


    #Solution to Part 2
    split_data = split_str_on_dont(input_data)
    split_data = split_str_on_do(split_data)
    split_data = remove_invalid_items(split_data)
    prepared_data = str(split_data)
    matches = extract_mul(prepared_data)
    result = mul_tuples_and_sum(matches)

    print(f'Pt2, sum of muls while do(): {result}')
