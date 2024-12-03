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
# idea is to split on don't(), insert a marker, split on do(), remove item directly after marker, and return string
def split_str_on_dont(input: str) -> list[str]:
    split_string = input.split("don't()")
    return split_string


def insert_between(lst: list[str]) -> list[str]:
    insert_str = 'ignore_next'
    result = []
    for item in lst:
        result.append(item)
        result.append(insert_str)
    return result


def split_str_on_do(input: list[str]) -> list[str]:
    result = []
    for item in input:
        split_string = item.split("do()")
        result.append(split_string)
    return result



def flatten_list_to_list(input: list[list[str]]) -> list[str]:
    result = []
    for item in input:
        for sub_item in item:
            result.append(sub_item)
    return result


def remove_incompatible_items(split_string: list[str]) -> list[str]:
    result = []
    for index, item in enumerate(split_string):
        if item == 'ignore_next':
            if index + 1 == len(split_string):
                continue
            else:
                split_string.pop(index + 1) # skip the next item
        else:
            result.append(item)
    return result


def flatten_list_to_string(input: list[str]) -> str:
    result = ''
    for item in input:
        result += item
    return result



### Solution to Part 2
if __name__ == "__main__":
    file_path = 'day3/input_data/input_data.txt'
    input = import_data(file_path)

    total = 0

    for line in input:
        split_string = split_str_on_dont(line)
        split_string = insert_between(split_string)
        split_string = split_str_on_do(split_string)
        split_string = flatten_list_to_list(split_string)
        split_string = remove_incompatible_items(split_string)
        split_string = flatten_list_to_string(split_string)
        matches = extract_mul(split_string)
        result = mul_tuples_and_sum(matches)
        total += result

    print(total)