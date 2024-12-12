
from day11.solution import split_even_numbers, run_algorithm

def test_split_evens():
    number = 17
    assert split_even_numbers(number, len(str(number))) == (1, 7)
    number = 123456
    assert split_even_numbers(number, len(str(number))) == (123, 456)
    number = 1000
    assert split_even_numbers(number, len(str(number))) == (10, 0)

def test_run_algorithm():
    initial_arrangement = [125, 17]
    total_blinks = 6
    result = [2097446912, 14168, 4048, 2, 0, 2, 4, 40, 48, 2024, 40, 48, 80, 96, 2, 8, 6, 7, 6, 0, 3, 2]
    assert run_algorithm(initial_arrangement, total_blinks) == result