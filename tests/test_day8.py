from day8.solution import subtract_tuples

# test the extract tuples function
def test_subtract_tuples():
    # test the extract tuples function
    tuple1 = (1, 1)
    tuple2 = (2, 2)
    assert subtract_tuples(tuple1, tuple2) == (-1, -1)

def test_subtract_tuples():
    # test the extract tuples function
    tuple1 = (2, 2)
    tuple2 = (-1, -1)
    assert subtract_tuples(tuple1, tuple2) == (3, 3)