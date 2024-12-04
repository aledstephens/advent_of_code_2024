import numpy as np
from collections import Counter


def load_input(file_path: str) -> list:

    with open(file_path) as f:
        data = f.read().splitlines()

    return data


def parse_input(data: list) -> tuple:
    '''
    Converts input to two lists of alternating integers
    '''
    lst1 = []
    lst2 = []

    for line in data:
        values = line.split('   ') # why is input seperator 3 spaces?
        lst1.append(int(values[0]))
        lst2.append(int(values[1]))

    return lst1, lst2


def compute_distance(lst1, lst2):
    lst1.sort()
    lst2.sort()
    distance = abs(np.subtract(lst1, lst2))
    total = np.sum(distance)
    return total


def similarity_score(lst1, lst2):
    '''
    After much faffing with numpy and pandas,
    I discovered the Counter class in the collections module,
    it made the solution much tidier.
    '''
    counts = Counter(lst2) # count the occurrences of each element in list2

    total = 0

    for element in lst1:
        if element in counts:
            total += element * counts[element] # multiply element by its count in list2
    return total


if __name__ == "__main__":
    input_data = load_input(file_path= 'day1/input_data/input.txt')
    list1, list2 = parse_input(input_data)

    result1 = compute_distance(list1, list2)
    print(f'distance total: {result1}')

    result2 = similarity_score(list1, list2)
    print(f'similarity score: {result2}')
