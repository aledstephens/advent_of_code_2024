from day12.solution import group_crops, calculate_perimeter
import numpy as np

def test_group_crops():
    data = [["A", "A", "A", "A"],
            ["B", "B", "C", "D"],
            ["B", "B", "C", "C"],
            ["E", "E", "E", "C"]]
    crops = np.array(data)
    plant_store = group_crops(crops)

    assert plant_store == {'A': {0: [(0, 0), (0, 1), (0, 2), (0, 3)]},
                            'B': {0: [(1, 0), (1, 1), (2, 0), (2, 1)]},
                            'C': {0: [(1, 2), (2, 2), (2, 3), (3, 3)]},
                            'D': {0: [(1, 3)]},
                            'E': {0: [(3, 0), (3, 1), (3, 2)]}
                           }


def test_group_crops_2():
    data = [["O", "O", "O", "O", "O"],
            ["O", "X", "O", "X", "O"],
            ["O", "O", "O", "O", "O"],
            ["O", "X", "O", "X", "O"],
            ["O", "O", "O", "O", "O"]]
    crops = np.array(data)
    plant_store = group_crops(crops)

    # make the assertion order not matter
    for key in plant_store:
        plant_store[key][0] = sorted(plant_store[key][0])


    assert plant_store == {'O': {0: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                                     (1, 0), (1, 2), (1, 4),
                                     (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                                     (3, 0), (3, 2), (3, 4),
                                     (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]},
                            'X': {0: [(1, 1)],
                                  1: [(1, 3)],
                                  2: [(3, 1)],
                                  3: [(3, 3)]}
                           }


def test_calculate_perimiter():
    plant_store = {'A': {0: [(0, 0), (0, 1), (1, 1)]},
                   'B': {0: [(1, 0)]},
                  }
    total = calculate_perimeter(plant_store)

    assert total == (3 * 8) + (1 * 4)