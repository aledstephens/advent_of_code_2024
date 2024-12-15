from day14.solution import load_data, move, valid_pos, find_quadrant, main_loop

def test_move():
    p = (2, 4)
    v = (1, -1)
    assert move(p, v) == (3, 3)


def test_valid_pos_in_bounds():
    p = (2, 2)
    lim = (3, 3)
    assert valid_pos(p, lim) == (2, 2)

def test_valid_pos_positive_wrap():
    p = (3, 3)
    lim = (3, 3)
    assert valid_pos(p, lim) == (0, 0)

def test_valid_pos_negative_wrap():
    p = (-1, -1)
    lim = (3, 3)
    assert valid_pos(p, lim) == (2, 2)


def test_find_quadrant_centre():
    pos = (3, 3)
    lim = (7, 7)
    assert find_quadrant(pos, lim) == 0

def test_find_quadrant_centre_horiz_line():
    pos = (1, 3)
    lim = (7, 7)
    assert find_quadrant(pos, lim) == 0

def test_find_quadrant_centre_vert_line():
    pos = (3, 1)
    lim = (7, 7)
    assert find_quadrant(pos, lim) == 0

def test_find_quadrant_top_left():
    pos = (1, 1)
    lim = (7, 7)
    assert find_quadrant(pos, lim) == 1

def test_find_quadrant_top_right():
    pos = (5, 1)
    lim = (7, 7)
    assert find_quadrant(pos, lim) == 2

def test_find_quadrant_bottom_left():
    pos = (1, 5)
    lim = (7, 7)
    assert find_quadrant(pos, lim) == 3

def test_find_quadrant_bottom_right():
    pos = (5, 5)
    lim = (7, 7)
    assert find_quadrant(pos, lim) == 4


def test_main_loop():
    data = load_data("../day14/input_data/input_test.txt")
    lim = (11, 7)
    seconds = 100
    product, location_store = main_loop(data, lim, seconds)
    assert product == 12

def test_main_loop_minimal():
    data = load_data("../day14/input_data/input_minimal.txt")
    lim = (11, 7)
    seconds = 5
    product, location_store = main_loop(data, lim, seconds)
    assert product == 0
