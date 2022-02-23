import sys

sys.path.append("../")
from insertion_sort import insertion_sort


def test_single_element_collection():
    input = [1]
    assert insertion_sort(input) == [1]


def test_sorted_collection():
    input = [1, 2, 3, 4, 5, 6]
    assert insertion_sort(input) == [1, 2, 3, 4, 5, 6]


def test_reversed_collection():
    input = [6, 5, 4, 3, 2, 1]
    assert insertion_sort(input) == [1, 2, 3, 4, 5, 6]


def test_shuffled_collection():
    input = [6, 1, 7, 9, 3, 8, 2, 5, 4, 0]
    assert insertion_sort(input) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
