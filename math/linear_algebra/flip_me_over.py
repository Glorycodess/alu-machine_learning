#!/usr/bin/env python3
"""Module to calculate the transpose of a 2D matrix."""


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix.

    Args:
        matrix (list of list): The original 2D matrix.

    Returns:
        list of list: The transposed matrix.
    """
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
