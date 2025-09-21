#!/usr/bin/env python3
"""
Add two 2D matrices element-wise.
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.

    Parameters:
        mat1 (list of list of int/float): first matrix
        mat2 (list of list of int/float): second matrix

    Returns:
        list: element-wise sum of mat1 and mat2
        None: if matrices are not the same shape
    """
    if len(mat1) != len(mat2):
        return None
    result = []
    for row1, row2 in zip(mat1, mat2):
        if len(row1) != len(row2):
            return None
        result.append([a + b for a, b in zip(row1, row2)])
    return result
