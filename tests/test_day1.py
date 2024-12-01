from day1.solution import compute_distance, similarity_score

def test_compute_distances():
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]
    expected_result = 11
    assert compute_distance(list1, list2) == expected_result

def test_similarity_score():
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]
    expected_result = 31
    assert similarity_score(list1, list2) == expected_result