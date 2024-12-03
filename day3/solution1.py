import re

# PART 1 Functions
def import_data(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        data = [line for line in file]
        return data


def extract_mul(input: str) -> list[tuple[str,str]]:
    '''
    Match this pattern: mul(X,Y) where X and Y are numbers
    '''

    pattern = r'mul\((\d+),(\d+)\)' # r is for raw string, \d is for digits, + is for 1 or more

    matches = re.findall(pattern, input)

    return matches


def mul_tuples_and_sum(input: list[tuple[str,str]]) -> list[int]:
    '''
    Multiply the tuples and return the sum
    '''
    result = []
    for tuple in input:
        result.append(int(tuple[0]) * int(tuple[1]))
    result = sum(result)
    return result

### Solution to Part 1
# if __name__ == "__main__":
#     file_path = 'day3/input_data/input_data.txt'
#     input = import_data(file_path)
#
#     total = 0
#
#     for line in input:
#         matches = extract_mul(line)
#         result = mul_tuples_and_sum(matches)
#         total += result
#
#     print(total)


# PART 2 Functions:
# idea is to split on don't() to get a list,
# split those lists on do(),
# ignore the first element of each sub-list
# but always keep the first list

def split_str_on_dont(input: str) -> list[str]:
    split_string = input.split("don't()")
    return split_string


def split_str_on_do(input: list[str]) -> list[str]:
    result = []
    for item in input:
        split_string = item.split("do()")
        result.append(split_string)
    return result


def remove_invalid_items(split_string: list[str]) -> list[str]:
    result = []
    for index, element in enumerate(split_string):
        if index == 0:  # always store first element
            result.append(element)
        elif len(element) > 1:  # longer elements have a do() so ignore first part
            result.append(element[1:])
        else:  # single elements are only a dont() so ignore
            continue

    return result


### Solution to Part 2
if __name__ == "__main__":
    file_path = 'input_data/input_data.txt'
    input = import_data(file_path)

    total = 0

    line = str(input) #treating the file as a single string worked
    split_string = split_str_on_dont(line)
    split_string = split_str_on_do(split_string)
    split_string = remove_invalid_items(split_string)
    split_string = str(split_string)
    matches = extract_mul(split_string)
    result = mul_tuples_and_sum(matches)
    total += result

    print(total)