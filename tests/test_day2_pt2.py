from day2.solution2 import count_safe_reports_with_damper

# test data
input = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
 ]

# expected output
expected = 4

# run the test
def test_safe_reports():
    safe_reports = count_safe_reports_with_damper(input)
    assert safe_reports == expected