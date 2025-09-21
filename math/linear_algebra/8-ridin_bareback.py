#!/usr/bin/env python3
"""
Matrix multiplication of two 2D matrices.
"""


def mat_mul(mat1, mat2):
    """
    Performs matrix multiplication of mat1 and mat2.

    Parameters:
        mat1 (list of list of int/float): first matrix
        mat2 (list of list of int/float): second matrix

    Returns:
        list: new matrix containing the product
        None: if matrices cannot be multiplied
    """
    # Number of columns in mat1 must equal number of rows in mat2
    if not mat1 or not mat2 or len(mat1[0]) != len(mat2):
        return None

    # Initialize result matrix with zeros
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]

    # Multiply
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result
