# This algorithm is taken from the GitHub repository: https://github.com/TheAlgorithms/Python

"""
This program print the matrix in spiral form.
This problem has been solved through recursive way.
      Matrix must satisfy below conditions
        i) matrix should be only one or two dimensional
        ii) number of column of all rows should be equal
"""

from collections.abc import Iterable

def check_matrix(matrix):
    # must be
    # decisions 1 and 2
    if matrix and isinstance(matrix, Iterable):
        # decision 3
        if isinstance(matrix[0], Iterable):
            prev_len = 0
            # decision 4
            for row in matrix:
                # decision 5
                if prev_len == 0:
                    prev_len = len(row)
                    result = True
                else:
                    result = prev_len == len(row)
        else:
            result = True
    else:
        result = False

    # exit 1
    return result

"""
lizard CCN: 6
Manual CCN:
    5 decisions
    1 exit
    CNN = 5 - 1 + 2 = 6
"""

def spiralPrint(a):
    # decisions 1 and 2
    if check_matrix(a) and len(a) > 0:
        matRow = len(a)
        # decision 3
        if isinstance(a[0], Iterable):
            matCol = len(a[0])
        else:
            # decision 4
            for dat in a:
                print(dat),
            # exit 1
            return

        # horizotal printing increasing
        # decision 5
        for i in range(0, matCol):
            print(a[0][i]),
        # vertical printing down
        # decision 6
        for i in range(1, matRow):
            print(a[i][matCol - 1]),
        # horizotal printing decreasing
        # decision 7
        if matRow > 1:
            # decision 8
            for i in range(matCol - 2, -1, -1):
                print(a[matRow - 1][i]),
        # vertical printing up
        # decision 9
        for i in range(matRow - 2, 0, -1):
            print(a[i][0]),
        # decision 10
        remainMat = [row[1 : matCol - 1] for row in a[1 : matRow - 1]]
        # decision 11
        if len(remainMat) > 0:
            spiralPrint(remainMat)
        else:
            # exit 2
            return
    else:
        print("Not a valid matrix")
        # exit 3
        return

"""
lizard CCN: 12
Manual CCN:
    11 decisions
    3 exits
    CNN = 11 - 3 + 2 = 10
"""