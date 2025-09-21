#!/usr/bin/env python3
"""
Transpose a 2D matrix
"""


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix

    Parameters:
        matrix (list of lists): 2D matrix to transpose

    Returns:
        list of lists: transposed matrix
    """
    # Use list comprehension to create the transpose
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
