from re import S
from numpy import random
from random import randint
import sys
sys.path.append('../')
from data_structure.coverage_tool import Coverage_tool
from data_structure.coverage_data_structure import CoverageData
from functions_analysed.strassen_coverage import strassen

# this test covers branch 1 (exception)
def test_exception(coverage: CoverageData):
    test_matrix1 = [[1], [1]]
    test_matrix2 = [[1], [1]]        
    try:
        strassen(test_matrix1, test_matrix2, coverage)
        assert False
    except Exception:
        assert True
    
# this test covers branches 2 and 3 (the matrix dimesions are equal)
def test_equal_dimensions(coverage: CoverageData):
    test_matrix1 = [[2, 2], [2, 2]]
    test_matrix2 = [[1, 1], [1, 1]]  
    assert strassen(test_matrix1, test_matrix2, coverage) == [test_matrix1, test_matrix2]

# this test covers branches 2,4-17
def test_no_error(coverage: CoverageData):
    test_matrix1 = [[1,2], [1,2], [1,2]]
    test_matrix2 = [[1,2,3], [1,2,3]]
    assert strassen(test_matrix1, test_matrix2, coverage) == [[3,6,9], [3,6,9], [3,6,9]]

if __name__ == "__main__":
    tests = [test_exception, test_equal_dimensions, test_no_error]
    coverageTool = Coverage_tool(tests, 17)
    coverageTool.run()
    coverageTool.print_results()