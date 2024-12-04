from day3.solution import *

def test_extract_mul():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    desired = [('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]

    result = extract_mul(input)

    assert result == desired


def test_mul_tuples_and_sum():
    input = [('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]
    desired = 161

    result = mul_tuples_and_sum(input)

    assert result == desired

def test_split_string_on_dont():
    input = "a string with 2 don't()s in it, also don't() here"
    desired = ['a string with 2 ',  's in it, also ', ' here']

    result = split_str_on_dont(input)

    assert result == desired


def test_part_2():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    split_string = split_str_on_dont(input)
    split_string = split_str_on_do(split_string)
    split_string = remove_invalid_items(split_string)
    split_string = str(split_string)
    matches = extract_mul(split_string)
    result = mul_tuples_and_sum(matches)

    assert result == 48

def test_part_2_mod():
    input = "do()xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+do()..do()mul(32,64)dont()..don't()(mul(11,8)undo()?mul(8,5))"
    split_string = split_str_on_dont(input)
    split_string = split_str_on_do(split_string)
    split_string = remove_invalid_items(split_string)
    split_string = str(split_string)
    matches = extract_mul(split_string)
    result = mul_tuples_and_sum(matches)

    desired = (2*4)+(32*64)+(8*5)
    assert result == desired