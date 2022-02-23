import sys
sys.path.append('../')
from spiral_print import spiralPrintTest

# test if a wrong matrix is detected
def test_wrong_matrix_1():
    spiralPrintTest([])
    f = open('spiralPrint.txt', 'r')
    assert f.read() == "Not a valid matrix\n"
    f.close()

def test_wrong_matrix_2():
    # find a test that enter branches 3, 4 and 5
    pass

# this test covers all non-errors branches
def test_no_error():
    matrix = ([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12])
    spiralPrintTest(matrix)
    f = open('spiralPrint.txt', 'r')
    assert f.read() == "1\n2\n3\n4\n8\n12\n11\n10\n9\n5\n6\n7\n"
    f.close()