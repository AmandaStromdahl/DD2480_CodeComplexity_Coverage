from collections.abc import Iterable
import sys
sys.path.append('../')
from data_structure.coverage_data_structure import CoverageData
# these imports are used for demonstration
# from numpy import random
# from random import randint
# from data_structure.coverage_tool import Coverage_tool

# This algorithm is taken from the GitHub repository: https://github.com/TheAlgorithms/Python

def check_matrix(matrix):
    if matrix and isinstance(matrix, Iterable):
        if isinstance(matrix[0], Iterable):
            prev_len = 0
            for row in matrix:
                if prev_len == 0:
                    prev_len = len(row)
                    result = True
                else:
                    result = prev_len == len(row)
        else:
            result = True
    else:
        result = False
    return result

def spiralPrint(a, coverage: CoverageData):
    if check_matrix(a) and len(a) > 0:
        coverage.log_branch("branch", 1)
        matRow = len(a)
        print(a)
        print(a[0])
        if isinstance(a[0], Iterable):
            coverage.log_branch("branch", 2)
            matCol = len(a[0])
        else:
            coverage.log_branch("branch", 3)
            for dat in a:
                coverage.log_branch("branch", 4)
                print(dat),
            coverage.log_branch("exit", 5)
            return
        coverage.log_branch("branch", 6)
        for i in range(0, matCol):
            coverage.log_branch("branch", 7)
            print(a[0][i]),
        for i in range(1, matRow):
            coverage.log_branch("branch", 8)
            print(a[i][matCol - 1]),
        coverage.log_branch("branch", 9)
        if matRow > 1:
            coverage.log_branch("branch", 10)
            for i in range(matCol - 2, -1, -1):
                coverage.log_branch("branch", 11)
                print(a[matRow - 1][i]),
        else:
            coverage.log_branch("branch", 12)
        coverage.log_branch("branch", 13)
        for i in range(matRow - 2, 0, -1):
            coverage.log_branch("branch", 14)
            print(a[i][0]),
        coverage.log_branch("branch", 15)
        remainMat = [row[1 : matCol - 1] for row in a[1 : matRow - 1]]
        if len(remainMat) > 0:
            coverage.log_branch("branch", 16)
            spiralPrint(remainMat, coverage)
        else:
            coverage.log_branch("exit", 17)
            return
        coverage.log_branch("branch", 18)
    else:
        coverage.log_branch("exit", 19)
        print("Not a valid matrix")
        return

def spiralPrintTest(a, coverage: CoverageData):
    original_stdout = sys.stdout
    f = open('spiralPrint.txt', 'w')
    sys.stdout = f
    spiralPrint(a, coverage)
    sys.stdout = original_stdout
    f.close()
    return

# The code below is kept in comments in case a demonstration is needed

# if __name__ == "__main__":
#     nb_run = 10
#     inputs = []
#     for i in range(nb_run):
#         matrix_size = randint(1, 100)
#         matrix = []
#         for i in range(matrix_size):
#             matrix.append(random.randint(100, size=(matrix_size)).tolist())
#         inputs.append(matrix)
#     coverage = Coverage_tool(nb_run, spiralPrint, inputs, 19)
#     coverage.run()
#     coverage.print_results()