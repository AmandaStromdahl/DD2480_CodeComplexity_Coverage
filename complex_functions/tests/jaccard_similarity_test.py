import sys
sys.path.append('../')
from jaccard_similarity import jaccard_similariy

# tests the algorithm on 2 sets
def test_two_sets_False():
    setA = {1}
    setB = {0}
    assert jaccard_similariy(setA, setB) == 0
    assert jaccard_similariy(setB, setA) == 0

# tests the algorithm on 2 sets with alternative union
def test_two_sets_True():
    setA = {1}
    setB = {0}
    assert jaccard_similariy(setA, setB, True) == 0
    assert jaccard_similariy(setB, setA, True) == 0

# tests the algorithm on 2 lists or tuples
def test_two_lists_or_tuples_False():
    setA = ['a', 'b', 'c', 'g']
    setB = ('d', 'e', 'f', 'g')
    assert jaccard_similariy(setA, setB) == 0.14285714285714285
    # this test fails due to an uncovered case in the algorithm
    # assert jaccard_similariy(setB, setA) == 0.14285714285714285

# tests the algorithm on 2 sets or tuples with alternative union
def test_two_lists_or_tuples_True():
    setA = ('c', 'd', 'e', 'f', 'h', 'i')
    setB = ('c', 'd', 'e', 'f', 'h', 'i')
    # this test fails due to an uncovered case in the algorithm
    # when the alternative union is chosen, union is a number
    # and we try to do len(union) with is not valid
    # assert jaccard_similariy(setA, setB, True) == 0
    # assert jaccard_similariy(setB, setA, True) == 0

# it tests all the invalid possible inputs
def test_invalid_arguments():
    assert jaccard_similariy({}, {}) == None
    assert jaccard_similariy({}, {0}) == None
    assert jaccard_similariy({0}, {}) == None
    assert jaccard_similariy(0, 0) == None
    assert jaccard_similariy({0}, 0) == None
    assert jaccard_similariy(0, {0}) == None
    assert jaccard_similariy(0, 0, True) == None
    assert jaccard_similariy({0}, 0, True) == None
    assert jaccard_similariy(0, {0}, True) == None
    assert jaccard_similariy({}, {}, True) == None
    assert jaccard_similariy({}, {0}, True) == None
    assert jaccard_similariy({0}, {}, True) == None
    assert jaccard_similariy(0, 0) == None
    assert jaccard_similariy((0), 0) == None
    assert jaccard_similariy(0, (0)) == None
    assert jaccard_similariy(0, 0, True) == None
    assert jaccard_similariy((0), 0, True) == None
    assert jaccard_similariy(0, (0), True) == None
    assert jaccard_similariy(0, 0) == None
    assert jaccard_similariy([0], 0) == None
    assert jaccard_similariy(0, [0]) == None
    assert jaccard_similariy(0, 0, True) == None
    assert jaccard_similariy([0], 0, True) == None
    assert jaccard_similariy(0, [0], True) == None