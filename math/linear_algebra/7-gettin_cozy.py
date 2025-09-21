#!/usr/bin/env python3
"""
Concatenate two 2D matrices along a specified axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along the specified axis.

    Parameters:
        mat1 (list of list of int/float): first matrix
        mat2 (list of list of int/float): second matrix
        axis (int): 0 to concatenate rows, 1 to concatenate columns

    Returns:
        list: new matrix containing concatenated result
        None: if matrices cannot be concatenated along the axis
    """
    if not mat1 or not mat2:
        return None

    # Concatenate rows (axis=0)
    if axis == 0:
        # Check same number of columns
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2

    # Concatenate columns (axis=1)
    elif axis == 1:
        # Check same number of rows
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]

    return None
