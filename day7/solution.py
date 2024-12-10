"""
Brute force way of solving part 1.
Randomly choosing the operations and checking if the result is equal to the value.
Took over 1000 loops for some of the test cases.
"""

import random

ops_types = ["mult", "add"]

def load_data(file_path: str) -> list:
    with open(file_path) as f:
        data = f.readlines()
    return data


def split_eq_into_test_value_and_elements(test_eq: str) -> tuple:
    test_value = test_eq.split(":")[0]
    test_value = int(test_value)
    elements = test_eq.split(":")[1].split(" ")
    elements = elements[1:]
    elements = [int(i) for i in elements]
    return test_value, elements


data = load_data("day7/input_data/input_full.txt")

main_counter = 0

for index,test_eq in enumerate(data):
    value, elements = split_eq_into_test_value_and_elements(test_eq)
    print(f"Test {index+1}")

    no_of_ops = len(elements) - 1

    loop_counter = 0
    result = 0

    while value != result:

        if loop_counter >= 10000:
            result = 0
            print("No solution found")
            break

        result = 0

        ops_chosen = [random.choice(ops_types) for i in range(no_of_ops)]

        result += elements[0]

        for i in range(no_of_ops):
            if ops_chosen[i] == "mult":
                result *= elements[i+1]
            else:
                result += elements[i+1]

        loop_counter += 1

    print(f"loops: {loop_counter}")

    main_counter += result

print(f"Total calibration result: {main_counter}")