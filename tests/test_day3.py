from day3.solution1 import extract_mul, mul_tuples_and_sum

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

