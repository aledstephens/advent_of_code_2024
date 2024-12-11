from day9.solution import convert_input, apportion_elements, calculate_checksum

def test_convert_input_simple():
    data = "12345"
    converted_assert = "0..111....22222"
    assert convert_input(data) == list(converted_assert)

def test_convert_input_multi_digit_index():
    """
    This was a stumbling point for me, had to modify code to account for multi-digit indexes.
    """
    data = "11" * 12
    converted_assert = ['0', '.', '1', '.', '2', '.', '3', '.', '4', '.', '5', '.', '6', '.', '7', '.', '8', '.', '9', '.', '10', '.', '11', '.']
    assert convert_input(data) == list(converted_assert)

#AOC test data
def test_convert_input_1():
    data = "2333133121414131402"
    converted_assert = "00...111...2...333.44.5555.6666.777.888899"
    assert convert_input(data) == list(converted_assert)

def test_apportion_elements_1():
    converted_assert = "00...111...2...333.44.5555.6666.777.888899"
    apportioned_assert =  "0099811188827773336446555566"
    assert apportion_elements(list(converted_assert)) == list(apportioned_assert)

def test_calcualte_checksum_1():
    apportioned_assert = "0099811188827773336446555566"
    checksum_assert = 1928
    assert calculate_checksum(list(apportioned_assert)) == checksum_assert

def test_all_1():
    data = "2333133121414131402"
    checksum_assert = 1928

    converted_input = convert_input(data)
    apportioned_elements = apportion_elements(converted_input)
    checksum = calculate_checksum(apportioned_elements)
    assert checksum == checksum_assert
