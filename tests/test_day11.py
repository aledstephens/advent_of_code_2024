
from day11.solution import split_even_numbers, run_algorithm

def test_split_evens():
    number = 17
    assert split_even_numbers(number, len(str(number))) == (1, 7)
    number = 123456
    assert split_even_numbers(number, len(str(number))) == (123, 456)
    number = 1000
    assert split_even_numbers(number, len(str(number))) == (10, 0)


def test_run_algorithm():
    initial_arrangement = {125:1, 17:1}
    total_blinks = 6
    result = {
        2097446912: 1,
        14168: 1,
        4048: 1,
        2: 4,
        0: 2,
        4: 1,
        40: 2,
        48: 2,
        2024: 1,
        80: 1,
        96: 1,
        8: 1,
        6: 2,
        7: 1,
        3: 1
    }

    assert run_algorithm(initial_arrangement, total_blinks) == result

def test_run_algorithm_2():
    initial_arrangement = [0, 0, 1, 1, 1000, 1000]
    total_blinks = 2

    # result_1_blink = {
    #     1: 2,
    #     2024: 2,
    #     10: 2,
    #     0: 2
    # }

    result_2_blink = {
        2024: 2,
        20: 2,
        24: 2,
        1: 4,
        0: 2,
    }

    assert run_algorithm(initial_arrangement, total_blinks) == result_2_blink
