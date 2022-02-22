from __future__ import annotations

import math

# This algorithm is taken from the GitHub repository: https://github.com/TheAlgorithms/Python

"""
# Original version

def strassen(matrix1: list, matrix2: list) -> list:
    if matrix_dimensions(matrix1)[1] != matrix_dimensions(matrix2)[0]:
        raise Exception(
            f"Unable to multiply these matrices, please check the dimensions. \n"
            f"Matrix A:{matrix1} \nMatrix B:{matrix2}"
        )
    dimension1 = matrix_dimensions(matrix1)
    dimension2 = matrix_dimensions(matrix2)

    if dimension1[0] == dimension1[1] and dimension2[0] == dimension2[1]:
        return [matrix1, matrix2]

    maximum = max(max(dimension1), max(dimension2))
    maxim = int(math.pow(2, math.ceil(math.log2(maximum))))
    new_matrix1 = matrix1
    new_matrix2 = matrix2

    # Adding zeros to the matrices so that the arrays dimensions are the same and also
    # power of 2
    
    for i in range(0, maxim):
        if i < dimension1[0]:
            for j in range(dimension1[1], maxim):
                new_matrix1[i].append(0)
        else:
            new_matrix1.append([0] * maxim)
        if i < dimension2[0]:
            for j in range(dimension2[1], maxim):
                new_matrix2[i].append(0)
        else:
            new_matrix2.append([0] * maxim)

    final_matrix = actual_strassen(new_matrix1, new_matrix2)

    # Removing the additional zeros
    
    for i in range(0, maxim):
        if i < dimension1[0]:
            for j in range(dimension2[1], maxim):
                final_matrix[i].pop()
        else:
            final_matrix.pop()
    return final_matrix
"""

# Refactored version
def strassen(matrix1: list, matrix2: list) -> list:
    if matrix_dimensions(matrix1)[1] != matrix_dimensions(matrix2)[0]:
        raise Exception(
            f"Unable to multiply these matrices, please check the dimensions. \n"
            f"Matrix A:{matrix1} \nMatrix B:{matrix2}"
        )
    dimension1 = matrix_dimensions(matrix1)
    dimension2 = matrix_dimensions(matrix2)

    if dimension1[0] == dimension1[1] and dimension2[0] == dimension2[1]:
        return [matrix1, matrix2]

    maximum = max(max(dimension1), max(dimension2))
    maxim = int(math.pow(2, math.ceil(math.log2(maximum))))
    new_matrix1 = matrix1
    new_matrix2 = matrix2

    # Adding zeros to the matrices so that the arrays dimensions are the same and also
    # power of 2
    
    # ----------------------------------------------------------------
    # REFACTORED: moved the appending of zeros to a separate function
    # ----------------------------------------------------------------
    new_matrix1 = matrixAppendZeros(dimension1, new_matrix1, maxim)
    new_matrix2 = matrixAppendZeros(dimension2, new_matrix2, maxim)
    # ----------------------------------------------------------------

    final_matrix = actual_strassen(new_matrix1, new_matrix2)

    # Removing the additional zeros
    # ----------------------------------------------------------------
    # REFACTORED: moved the removal of zeros to a separate function
    # ----------------------------------------------------------------
    final_matrix = matrixRemoveAdditionalZeros(final_matrix, dimension1[0], dimension2[1], maxim)
    # ----------------------------------------------------------------
    
    return final_matrix

# ----------------------------------------------------------------
# REFACTORED: moved code from strassen() into this helper function
# ----------------------------------------------------------------
def matrixAppendZeros(dimension: list, matrix: list, maxim: int) -> list:
    for i in range(0, maxim):
        if i < dimension[0]:
            for j in range(dimension[1], maxim):
                matrix[i].append(0)
        else:
            matrix.append([0] * maxim)
            
    return matrix
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# REFACTORED: moved code from strassen() into this helper function
# ----------------------------------------------------------------
def matrixRemoveAdditionalZeros(final_matrix: list, dim1: int, dim2: int, maxim) -> list:
    for i in range(0, maxim):
        if i < dim1:
            for j in range(dim2, maxim):
                final_matrix[i].pop()
        else:
            final_matrix.pop()
            
    return final_matrix
# ----------------------------------------------------------------


    """
    Lizard CCN, original version of strassen(): 12
    Lizard CCN, refactored version strassen(): 4  => approx. 67% cyclomatic complexity reduction
    (Lizard CCN, matrixAppendZeros(): 4)
    (Lizard CCN, matrixRemoveAdditionalZeros(): 4)
    
    Manual CCN, original version of strassen(): 10
    Manual CCN, refactored version of strassen(): 2  (3 decisions, 3 exits)
    (Manual CCN, matrixAppendZeros(): 4 (3 decisions, 1 exit))
    (Manual CCN, matrixRemoveAdditionalZeros(): 4 (3 decisions, 1 exit))
    """

