import sys
sys.path.append('../')
from spiral_print import spiralPrintTest

'''
Global note:
In order to test this function, I created an intermediate function
called spiralPrintTest that you can found in complex_functions/spiral_print.py
that redirect the output into a text file that is used to analyse the
output of the function
'''

'''
The spiralPrint() method should not compute/print an invalid
matrix. This test tries to run the method with an empty array,
which is an invalid input. The method should print an error
message in the terminal
'''
def test_wrong_matrix_1():
    spiralPrintTest([])
    f = open('spiralPrint.txt', 'r')
    assert f.read() == "Not a valid matrix\n"
    f.close()

'''
After spending time on this test, I could not find any input
that will enter branches 3, 4 and 5. Theses 3 branches are the
only ones missing to get a 100% branch coverage
'''
def test_wrong_matrix_2():
    # find a test that enter branches 3, 4 and 5
    pass

'''
The spiralPrint() method should print the values of a matrix
in the right order in terms of a spiral starting from (0, 0)
and going to the right: (0, 0) -> (0, 1) -> (0, 2) -> ...
Note: (row, column)
This test runs the spiralPrint() method on a specific input that
has the particularity that it covers all the non-error branches
of the method
'''
def test_no_error():
    matrix = ([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12])
    spiralPrintTest(matrix)
    f = open('spiralPrint.txt', 'r')
    assert f.read() == "1\n2\n3\n4\n8\n12\n11\n10\n9\n5\n6\n7\n"
    f.close()