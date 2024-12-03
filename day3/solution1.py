import re

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

if __name__ == "__main__":
    file_path = 'day3/input_data/input_data.txt'
    input = import_data(file_path)

    total = 0

    for line in input:
        matches = extract_mul(line)
        result = mul_tuples_and_sum(matches)
        total += result

    print(total)

