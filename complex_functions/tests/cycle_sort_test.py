from numpy import random
from random import randint
import sys
sys.path.append('../')
from cycle_sort import cycle_sort

# this test covers all branches
def test_all_branches():
    test_list = [54, 50, 57, 33, 50, 50, 8, 31, 13, 2]
    assert cycle_sort(test_list) == sorted(test_list)

# this test run the algorithm on a random list
def test_random_list():
    test_list = random.randint(100, size=(randint(1, 100))).tolist()
    assert cycle_sort(test_list) == sorted(test_list)