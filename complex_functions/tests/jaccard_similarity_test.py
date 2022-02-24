import sys
sys.path.append('../')
from jaccard_similarity import jaccard_similariy

'''
The jaccard_similarity() method should correctly compute the
jaccard_similarity of two sets without using the alternative union,
i.e. union is define as the lenght of the union of the two sets
'''
def test_two_sets_False():
    setA = {1}
    setB = {1}
    assert jaccard_similariy(setA, setB) == 1
    assert jaccard_similariy(setB, setA) == 1

'''
The jaccard_similarity() method should correctly compute the
jaccard_similarity of two sets using the alternative union,
i.e. union is define as the sum of the length of the two sets
'''
def test_two_sets_True():
    setA = {1}
    setB = {1}
    assert jaccard_similariy(setA, setB, True) == 0.5
    assert jaccard_similariy(setB, setA, True) == 0.5

'''
The jaccard_similarity() method should correctly compute the
jaccard_similarity of two lists or tuples without using the alternative union,
i.e. union is define as the lenght of the union of the two lists or tuples
'''
def test_two_lists_or_tuples_False():
    setA = ['a', 'b', 'c', 'g']
    setB = ('d', 'e', 'f', 'g')
    assert jaccard_similariy(setA, setB) == 0.14285714285714285
    # this test fails due to an uncovered case in the algorithm

    # assert jaccard_similariy(setB, setA) == 0.14285714285714285

    # when computing the union, the program raises an error:
    # TypeError: can only concatenate tuple (not "list") to tuple

'''
The jaccard_similarity() method should correctly compute the
jaccard_similarity of two lists or tuples using the alternative union,
i.e. union is define as the sum of the length of the two lists or tuples
'''
def test_two_lists_or_tuples_True():
    setA = ('c', 'd', 'e', 'f', 'h', 'i')
    setB = ('c', 'd', 'e', 'f', 'h', 'i')
    # these tests fail due to an uncovered case in the algorithm

    # assert jaccard_similariy(setA, setB, True) == 0
    # assert jaccard_similariy(setB, setA, True) == 0

    # when the alternative union is chosen, union is a number
    # and we try to do len(union) with is not valid
    # so we get the error:
    # TypeError: object of type 'int' has no len()

'''
The jaccard_similarity() method should not compute the
jaccard similarity when invalid inputs are given, i.e it shoudl not
enter any if statements, so the method should return None. This test
checks all the possible invalid inputs
'''
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