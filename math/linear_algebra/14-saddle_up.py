#!/usr/bin/env python3
"""Module to perform matrix multiplication using NumPy."""

import numpy as np


def np_matmul(mat1, mat2):
    """
    Perform matrix multiplication between two numpy arrays.

    Args:
        mat1 (numpy.ndarray): First matrix.
        mat2 (numpy.ndarray): Second matrix.

    Returns:
        numpy.ndarray: Result of matrix multiplication.
    """
    return np.matmul(mat1, mat2)
