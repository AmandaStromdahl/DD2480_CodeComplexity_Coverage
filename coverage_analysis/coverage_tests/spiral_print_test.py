from typing import Iterable
from numpy import random
from random import randint
import sys
sys.path.append('../')
from data_structure.coverage_tool import Coverage_tool
from data_structure.coverage_data_structure import CoverageData
from functions_analysed.spiral_print_coverage import spiralPrintTest

# test if a wrong matrix is detected
def test_wrong_matrix_1(coverage: CoverageData):
    spiralPrintTest([], coverage)
    f = open('spiralPrint.txt', 'r')
    assert f.read() == "Not a valid matrix\n"
    f.close()

def test_wrong_matrix_2(coverage: CoverageData):
    # find a test that enter branches 3, 4 and 5
    pass

# this test covers all non-errors branches
def test_no_error(coverage: CoverageData):
    matrix = ([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12])
    spiralPrintTest(matrix, coverage)
    f = open('spiralPrint.txt', 'r')
    assert f.read() == "1\n2\n3\n4\n8\n12\n11\n10\n9\n5\n6\n7\n"
    f.close()

if __name__ == "__main__":
    tests = [test_wrong_matrix_1, test_no_error]
    coverageTool = Coverage_tool(tests, 19)
    coverageTool.run()
    coverageTool.print_results()