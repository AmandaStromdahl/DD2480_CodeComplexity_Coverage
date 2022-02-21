from __future__ import annotations

import math

# This algorithm is taken from the GitHub repository: https://github.com/TheAlgorithms/Python

def strassen(matrix1: list, matrix2: list) -> list:
    
    # Decision 1
    if matrix_dimensions(matrix1)[1] != matrix_dimensions(matrix2)[0]:
        # Exit 1
        raise Exception(
            f"Unable to multiply these matrices, please check the dimensions. \n"
            f"Matrix A:{matrix1} \nMatrix B:{matrix2}"
        )
    dimension1 = matrix_dimensions(matrix1)
    dimension2 = matrix_dimensions(matrix2)

    # Decisions 2 and 3
    if dimension1[0] == dimension1[1] and dimension2[0] == dimension2[1]:
        # Exit 2
        return [matrix1, matrix2]

    maximum = max(max(dimension1), max(dimension2))
    maxim = int(math.pow(2, math.ceil(math.log2(maximum))))
    new_matrix1 = matrix1
    new_matrix2 = matrix2

    # Adding zeros to the matrices so that the arrays dimensions are the same and also
    # power of 2
    
    # Decision 4
    for i in range(0, maxim):
        # Decision 5
        if i < dimension1[0]:
            # Decision 6
            for j in range(dimension1[1], maxim):
                new_matrix1[i].append(0)
        else:
            new_matrix1.append([0] * maxim)
        # Decision 7
        if i < dimension2[0]:
            # Decision 8
            for j in range(dimension2[1], maxim):
                new_matrix2[i].append(0)
        else:
            new_matrix2.append([0] * maxim)

    final_matrix = actual_strassen(new_matrix1, new_matrix2)

    # Removing the additional zeros
    
    # Decision 9
    for i in range(0, maxim):
        # Decision 10
        if i < dimension1[0]:
            # Decision 11
            for j in range(dimension2[1], maxim):
                final_matrix[i].pop()
        else:
            final_matrix.pop()
    # Exit 3
    return final_matrix

    """
    Lizard CCN: 12
    Manual CCN: 10
        11 decisions
        3 exits
        CCN = 11 - 3 + 2 = 10
    """
